# -*- coding: utf-8 -*- #
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Provides common arguments for the ML Engine command surface."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import argparse
import functools
import itertools
import sys

from googlecloudsdk.api_lib.ml_engine import versions_api
from googlecloudsdk.api_lib.storage import storage_util
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope.concepts import concepts
from googlecloudsdk.command_lib.iam import completers as iam_completers
from googlecloudsdk.command_lib.ml_engine import models_util
from googlecloudsdk.command_lib.projects import resource_args as project_resource_args
from googlecloudsdk.command_lib.util.apis import arg_utils
from googlecloudsdk.command_lib.util.args import repeated
from googlecloudsdk.command_lib.util.args import update_util
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


_JOB_SUMMARY = """\
table[box,title="Job Overview"](
  jobId,
  createTime,
  startTime,
  endTime,
  state,
  {INPUT},
  {OUTPUT})
"""

_JOB_TRAIN_INPUT_SUMMARY_FORMAT = """\
trainingInput:format='table[box,title="Training Input Summary"](
  runtimeVersion:optional,
  region,
  scaleTier:optional,
  pythonModule,
  parameterServerType:optional,
  parameterServerCount:optional,
  masterType:optional,
  workerType:optional,
  workerCount:optional,
  jobDir:optional
)'
"""

_JOB_TRAIN_OUTPUT_SUMMARY_FORMAT = """\
trainingOutput:format='table[box,title="Training Output Summary"](
  completedTrialCount:optional:label=TRIALS,
  consumedMLUnits:label=ML_UNITS)'
  {HP_OUTPUT}
"""

_JOB_TRAIN_OUTPUT_TRIALS_FORMAT = """\
,trainingOutput.trials.sort(trialId):format='table[box,title="Training Output Trials"](
  trialId:label=TRIAL,
  finalMetric.objectiveValue:label=OBJECTIVE_VALUE,
  finalMetric.trainingStep:label=STEP,
  hyperparameters.list(separator="\n"))'
"""

_JOB_PREDICT_INPUT_SUMMARY_FORMAT = """\
predictionInput:format='table[box,title="Predict Input Summary"](
  runtimeVersion:optional,
  region,
  model.basename():optional,
  versionName.basename(),
  outputPath,
  uri:optional,
  dataFormat,
  batchSize:optional
)'
"""

_JOB_PREDICT_OUTPUT_SUMMARY_FORMAT = """\
predictionOutput:format='table[box,title="Predict Output Summary"](
  errorCount,
  nodeHours,
  outputPath,
  predictionCount
  )'
"""


class ArgumentError(exceptions.Error):
  pass


class MlEngineIamRolesCompleter(iam_completers.IamRolesCompleter):

  def __init__(self, **kwargs):
    super(MlEngineIamRolesCompleter, self).__init__(
        resource_collection=models_util.MODELS_COLLECTION,
        resource_dest='model',
        **kwargs)


def GetDescriptionFlag(noun):
  return base.Argument(
      '--description',
      required=False,
      default=None,
      help='The description of the {noun}.'.format(noun=noun))

# Run flags
DISTRIBUTED = base.Argument(
    '--distributed',
    action='store_true',
    default=False,
    help=('Runs the provided code in distributed mode by providing cluster '
          'configurations as environment variables to subprocesses'))
PARAM_SERVERS = base.Argument(
    '--parameter-server-count',
    type=int,
    help=('Number of parameter servers with which to run. '
          'Ignored if --distributed is not specified. Default: 2'))
WORKERS = base.Argument(
    '--worker-count',
    type=int,
    help=('Number of workers with which to run. '
          'Ignored if --distributed is not specified. Default: 2'))
START_PORT = base.Argument(
    '--start-port',
    type=int,
    default=27182,
    help="""\
Start of the range of ports reserved by the local cluster. This command will use
a contiguous block of ports equal to parameter-server-count + worker-count + 1.

If --distributed is not specified, this flag is ignored.
""")


OPERATION_NAME = base.Argument('operation', help='Name of the operation.')


CONFIG = base.Argument(
    '--config',
    help="""\
Path to the job configuration file. The file should be a YAML document (JSON
also accepted) containing a Job resource as defined in the API (all fields are
optional): https://cloud.google.com/ml/reference/rest/v1/projects.jobs

If an option is specified both in the configuration file *and* via command line
arguments, the command line arguments override the configuration file.
""")
JOB_NAME = base.Argument('job', help='Name of the job.')
MODULE_NAME = base.Argument(
    '--module-name',
    required=True,
    help='Name of the module to run')
PACKAGE_PATH = base.Argument(
    '--package-path',
    help="""\
Path to a Python package to build. This should point to a directory containing
the Python source for the job. It will be built using setuptools (which must be
installed) using its *parent* directory as context. If the parent directory
contains a `setup.py` file, the build will use that; otherwise, it will use a
simple built-in one.
""")
PACKAGES = base.Argument(
    '--packages',
    default=[],
    type=arg_parsers.ArgList(),
    metavar='PACKAGE',
    help="""\
Path to Python archives used for training. These can be local paths
(absolute or relative), in which case they will be uploaded to the Cloud
Storage bucket given by `--staging-bucket`, or Cloud Storage URLs
(`gs://bucket-name/path/to/package.tar.gz`).
""")
# As of Alpha/Beta release, the backend service processes this as a string
# (despite having only 2 valid values). It is a string here since there is no
# enum validation but can be refactored if that changes before GA.
MACHINE_TYPE = base.Argument(
    '--machine-type',
    required=False,
    help="""\
The type of machine on which to serve the model. Currently only applies to
online prediction. Currently supported machine_types are:

* `mls1-c1-m2` - A virtual machine with 1 core and 2 Gb RAM (default).
* `mls1-c4-m2` - A virtual machine with 4 core and 2 Gb RAM.
""")
ALPHA_MACHINE_TYPE = base.Argument(
    '--machine-type',
    required=False,
    help="""\
The type of machine on which to serve the model. Currently only applies to
online prediction. Currently supported machine_types are:

* `mls1-c1-m2` - A virtual machine with 1 core and 2 Gb RAM (default).
* `mls1-c4-m2` - A virtual machine with 4 core and 2 Gb RAM.
* `mls1-highmem-1` - A virtual machine with 1 core and 2 Gb RAM (will be deprecated soon).
* `mls1-highcpu-4` - A virtual machine with 4 core and 2 Gb RAM (will be deprecated soon).
""")


def GetJobDirFlag(upload_help=True, allow_local=False):
  """Get base.Argument() for `--job-dir`.

  If allow_local is provided, this Argument gives a str when parsed; otherwise,
  it gives a (possibly empty) ObjectReference.

  Args:
    upload_help: bool, whether to include help text related to object upload.
      Only useful in remote situations (`jobs submit training`).
    allow_local: bool, whether to allow local directories (only useful in local
      situations, like `local train`) or restrict input to directories in Cloud
      Storage.

  Returns:
    base.Argument() for the corresponding `--job-dir` flag.
  """
  help_ = """\
A {dir_type} in which to store training outputs and other data
needed for training.

This path will be passed to your TensorFlow program as `--job_dir` command-line
arg. The benefit of specifying this field is that Cloud ML Engine will validate
the path for use in training.
""".format(dir_type=('Google Cloud Storage path' +
                     (' or local_directory' if allow_local else '')))
  if upload_help:
    help_ += """\

If packages must be uploaded and `--staging-bucket` is not provided, this path
will be used instead.
"""

  if allow_local:
    type_ = str
  else:
    type_ = functools.partial(storage_util.ObjectReference.FromArgument,
                              allow_empty_object=True)  # pytype: disable=wrong-arg-types
  return base.Argument('--job-dir', type=type_, help=help_)


def GetUserArgs(local=False):
  if local:
    help_text = """\
Additional user arguments to be forwarded to user code. Any relative paths will
be relative to the *parent* directory of `--package-path`.
"""
  else:
    help_text = 'Additional user arguments to be forwarded to user code'
  return base.Argument(
      'user_args',
      nargs=argparse.REMAINDER,
      help=help_text)


VERSION_NAME = base.Argument('version', help='Name of the model version.')

RUNTIME_VERSION = base.Argument(
    '--runtime-version',
    help=(
        'The Google Cloud ML Engine runtime version for this job. Defaults '
        'to a stable version, which is defined in the documentation along '
        'with the list of supported versions: '
        'https://cloud.google.com/ml-engine/docs/tensorflow/runtime-version-list'  # pylint: disable=line-too-long
    ))


POLLING_INTERVAL = base.Argument(
    '--polling-interval',
    type=arg_parsers.BoundedInt(1, sys.maxsize, unlimited=True),
    required=False,
    default=60,
    action=actions.StoreProperty(properties.VALUES.ml_engine.polling_interval),
    help='Number of seconds to wait between efforts to fetch the latest '
    'log messages.')
ALLOW_MULTILINE_LOGS = base.Argument(
    '--allow-multiline-logs',
    action='store_true',
    help='Output multiline log messages as single records.')
TASK_NAME = base.Argument(
    '--task-name',
    required=False,
    default=None,
    help='If set, display only the logs for this particular task.')


_FRAMEWORK_CHOICES = {
    'TENSORFLOW': 'tensorflow',
    'SCIKIT_LEARN': 'scikit-learn',
    'XGBOOST': 'xgboost'
}
FRAMEWORK_MAPPER = arg_utils.ChoiceEnumMapper(
    '--framework',
    (versions_api.GetMessagesModule().
     GoogleCloudMlV1Version.FrameworkValueValuesEnum),
    custom_mappings=_FRAMEWORK_CHOICES,
    help_str=('The ML framework used to train this version of the model. '
              'If not specified, defaults to `tensorflow`'))


def AddPythonVersionFlag(parser, context):
  help_str = (
      'The version of Python used {context}. If not set, the default '
      'version is 2.7. Python 3.5 is available when `runtime_version` is '
      'set to 1.4 and above. Python 2.7 works with all supported runtime '
      'versions.').format(context=context)
  version = base.Argument(
      '--python-version',
      help=help_str)
  version.AddToParser(parser)


def GetModelName(positional=True, required=False):
  help_text = 'Name of the model.'
  if positional:
    return base.Argument('model', help=help_text)
  else:
    return base.Argument('--model', help=help_text, required=required)


# TODO(b/33234717): remove after PACKAGES nargs=+ deprecation period.
def ProcessPackages(args):
  """Flatten PACKAGES flag and warn if multiple arguments were used."""
  if args.packages is not None:
    if len(args.packages) > 1:
      log.warning('Use of --packages with space separated values is '
                  'deprecated and will not work in the future. Use comma '
                  'instead.')
    # flatten packages into a single list
    args.packages = list(itertools.chain.from_iterable(args.packages))


STAGING_BUCKET = base.Argument(
    '--staging-bucket',
    type=storage_util.BucketReference.FromArgument,
    help="""\
        Bucket in which to stage training archives.

        Required only if a file upload is necessary (that is, other flags
        include local paths) and no other flags implicitly specify an upload
        path.
        """)


def GetSummarizeFlag():
  return base.Argument(
      '--summarize',
      action='store_true',
      required=False,
      help="""\
      Summarize job output in a set of human readable tables instead of
      rendering the entire resource as json or yaml. The tables currently rendered
      are:

      * `Job Overview`: Overview of job including, jobId, status and create time.
      * `Training Input Summary`: Summary of input for a training job including
         region, main training python module and scale tier.
      * `Training Output Summary`: Summary of output for a training job including
         the amount of ML units consumed by the job.
      * `Training Output Trials`: Summary of hyperparameter trials run for a
         hyperparameter tuning training job.
      * `Predict Input Summary`: Summary of input for a prediction job including
         region, model verion and output path.
      * `Predict Output Summary`: Summary of output for a prediction job including
         prediction count and output path.

      This flag overrides the `--format` flag. If
      both are present on the command line, a warning is displayed.
      """)


def GetStandardTrainingJobSummary():
  """Get tabular format for standard ml training job."""
  return _JOB_SUMMARY.format(
      INPUT=_JOB_TRAIN_INPUT_SUMMARY_FORMAT,
      OUTPUT=_JOB_TRAIN_OUTPUT_SUMMARY_FORMAT.format(HP_OUTPUT=''))


def GetHPTrainingJobSummary():
  """Get tablular format to HyperParameter tuning ml job."""
  return _JOB_SUMMARY.format(
      INPUT=_JOB_PREDICT_INPUT_SUMMARY_FORMAT,
      OUTPUT=_JOB_TRAIN_OUTPUT_SUMMARY_FORMAT.format(
          HP_OUTPUT=_JOB_TRAIN_OUTPUT_TRIALS_FORMAT))


def GetPredictJobSummary():
  """Get table format for ml prediction job."""
  return _JOB_SUMMARY.format(
      INPUT=_JOB_PREDICT_INPUT_SUMMARY_FORMAT,
      OUTPUT=_JOB_PREDICT_OUTPUT_SUMMARY_FORMAT)


def ModelAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='model',
      help_text='The model for the {resource}.')


def VersionAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='version',
      help_text='The version for the {resource}.')


def GetVersionResourceSpec():
  return concepts.ResourceSpec(
      'ml.projects.models.versions',
      resource_name='version',
      versionsId=VersionAttributeConfig(),
      modelsId=ModelAttributeConfig(),
      projectsId=project_resource_args.PROJECT_ATTRIBUTE_CONFIG)


def AddVersionResourceArg(parser, verb):
  """Add a resource argument for a Cloud ML Engine version."""
  concept_parsers.ConceptParser.ForResource(
      'version',
      GetVersionResourceSpec(),
      'The Cloud ML Engine model {}.'.format(verb),
      required=True).AddToParser(parser)


def AddUserCodeArgs(parser):
  """Add args that configure user prediction code."""
  user_code_group = base.ArgumentGroup(
      help="""\
          Configure user code in prediction.

          Cloud ML Engine allows a model to have user-provided prediction
          code; these options configure that code.
          """)
  user_code_group.AddArgument(base.Argument(
      '--model-class',
      help="""\
          The fully-qualified name of the custom Model class in the package
          provided for custom prediction.

          For example, `--model-class my_package.SequenceModel`.
          """))
  user_code_group.AddArgument(base.Argument(
      '--package-uris',
      type=arg_parsers.ArgList(),
      metavar='PACKAGE_URI',
      help="""\
          Comma-separated list of Google Cloud Storage URIs (`gs://...`) for
          user-supplied Python packages to use.
          """))
  user_code_group.AddToParser(parser)


def AddUserCodeUpdateArgs(parser):
  """Add args that configure user prediction code."""
  user_code_group = parser.add_group(
      help="""\
          Configure user code in prediction.

          Cloud ML Engine allows a model to have user-provided prediction
          code; these options configure that code.
          """)
  repeated.AddPrimitiveArgs(
      user_code_group, 'version', 'package-uris',
      'user-supplied packages to use for prediction',
      additional_help=('The values should be given as a comma-separated list '
                       'of Google Cloud Storage URIs (`gs://...`).'))
  update_util.AddClearableField(
      user_code_group, 'model-class', 'custom Model class', 'version',
      ('The fully-qualified name of the custom Model class in the package '
       'provided for custom prediction.\n\n'
       'For example, `my_package.SequenceModel`.'))

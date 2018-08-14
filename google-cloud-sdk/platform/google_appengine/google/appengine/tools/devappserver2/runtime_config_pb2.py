#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apphosting/tools/devappserver2/runtime_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
import google
from google.net.proto2.python.public import descriptor as _descriptor
from google.net.proto2.python.public import message as _message
from google.net.proto2.python.public import reflection as _reflection
from google.net.proto2.python.public import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apphosting/tools/devappserver2/runtime_config.proto',
  package='apphosting.tools.devappserver2',
  syntax='proto2',
  serialized_options=_b('\n,com.google.appengine.tools.development.proto \002P\001'),
  serialized_pb=_b('\n3apphosting/tools/devappserver2/runtime_config.proto\x12\x1e\x61pphosting.tools.devappserver2\"\xee\x07\n\x06\x43onfig\x12\x0e\n\x06\x61pp_id\x18\x01 \x02(\x0c\x12\x12\n\nversion_id\x18\x02 \x02(\x0c\x12\x18\n\x10\x61pplication_root\x18\x03 \x02(\x0c\x12\x19\n\nthreadsafe\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x08\x61pi_host\x18\x11 \x01(\t:\tlocalhost\x12\x10\n\x08\x61pi_port\x18\x05 \x02(\x05\x12:\n\tlibraries\x18\x06 \x03(\x0b\x32\'.apphosting.tools.devappserver2.Library\x12\x16\n\nskip_files\x18\x07 \x01(\t:\x02^$\x12\x18\n\x0cstatic_files\x18\x08 \x01(\t:\x02^$\x12\x43\n\rpython_config\x18\x0e \x01(\x0b\x32,.apphosting.tools.devappserver2.PythonConfig\x12=\n\nphp_config\x18\t \x01(\x0b\x32).apphosting.tools.devappserver2.PhpConfig\x12?\n\x0bnode_config\x18\x1a \x01(\x0b\x32*.apphosting.tools.devappserver2.NodeConfig\x12?\n\x0bjava_config\x18\x15 \x01(\x0b\x32*.apphosting.tools.devappserver2.JavaConfig\x12\x43\n\rcustom_config\x18\x17 \x01(\x0b\x32,.apphosting.tools.devappserver2.CustomConfig\x12;\n\tgo_config\x18\x19 \x01(\x0b\x32(.apphosting.tools.devappserver2.GoConfig\x12\x38\n\x07\x65nviron\x18\n \x03(\x0b\x32\'.apphosting.tools.devappserver2.Environ\x12\x42\n\x10\x63loud_sql_config\x18\x0b \x01(\x0b\x32(.apphosting.tools.devappserver2.CloudSQL\x12\x12\n\ndatacenter\x18\x0c \x02(\t\x12\x13\n\x0binstance_id\x18\r \x02(\t\x12\x1b\n\x10stderr_log_level\x18\x0f \x01(\x03:\x01\x31\x12\x13\n\x0b\x61uth_domain\x18\x10 \x02(\t\x12\x15\n\rmax_instances\x18\x12 \x01(\x05\x12;\n\tvm_config\x18\x13 \x01(\x0b\x32(.apphosting.tools.devappserver2.VMConfig\x12\x13\n\x0bserver_port\x18\x14 \x01(\x05\x12\x11\n\x02vm\x18\x16 \x01(\x08:\x05\x66\x61lse\x12\x11\n\tgrpc_apis\x18\x18 \x03(\t\"\x91\x01\n\tPhpConfig\x12\x1b\n\x13php_executable_path\x18\x01 \x01(\x0c\x12\x17\n\x0f\x65nable_debugger\x18\x03 \x02(\x08\x12\x1a\n\x12gae_extension_path\x18\x04 \x01(\x0c\x12\x1d\n\x15xdebug_extension_path\x18\x05 \x01(\x0c\x12\x13\n\x0bphp_version\x18\x06 \x01(\x0c\"*\n\nNodeConfig\x12\x1c\n\x14node_executable_path\x18\x01 \x01(\x0c\"<\n\x0cPythonConfig\x12\x16\n\x0estartup_script\x18\x01 \x01(\t\x12\x14\n\x0cstartup_args\x18\x02 \x01(\t\"\x1e\n\nJavaConfig\x12\x10\n\x08jvm_args\x18\x01 \x03(\t\"W\n\x08GoConfig\x12\x10\n\x08work_dir\x18\x01 \x01(\t\x12\x1f\n\x17\x65nable_watching_go_path\x18\x02 \x01(\x08\x12\x18\n\x10\x65nable_debugging\x18\x03 \x01(\x08\":\n\x0c\x43ustomConfig\x12\x19\n\x11\x63ustom_entrypoint\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\x02 \x01(\t\"t\n\x08\x43loudSQL\x12\x12\n\nmysql_host\x18\x01 \x02(\t\x12\x12\n\nmysql_port\x18\x02 \x02(\x05\x12\x12\n\nmysql_user\x18\x03 \x02(\t\x12\x16\n\x0emysql_password\x18\x04 \x02(\t\x12\x14\n\x0cmysql_socket\x18\x05 \x01(\t\"(\n\x07Library\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0f\n\x07version\x18\x02 \x02(\t\"%\n\x07\x45nviron\x12\x0b\n\x03key\x18\x01 \x02(\x0c\x12\r\n\x05value\x18\x02 \x02(\x0c\":\n\x08VMConfig\x12\x19\n\x11\x64ocker_daemon_url\x18\x01 \x01(\t\x12\x13\n\x0b\x65nable_logs\x18\x03 \x01(\x08\x42\x32\n,com.google.appengine.tools.development.proto \x02P\x01')
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='apphosting.tools.devappserver2.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_id', full_name='apphosting.tools.devappserver2.Config.app_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_id', full_name='apphosting.tools.devappserver2.Config.version_id', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='application_root', full_name='apphosting.tools.devappserver2.Config.application_root', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threadsafe', full_name='apphosting.tools.devappserver2.Config.threadsafe', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_host', full_name='apphosting.tools.devappserver2.Config.api_host', index=4,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("localhost").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_port', full_name='apphosting.tools.devappserver2.Config.api_port', index=5,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='libraries', full_name='apphosting.tools.devappserver2.Config.libraries', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skip_files', full_name='apphosting.tools.devappserver2.Config.skip_files', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("^$").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='static_files', full_name='apphosting.tools.devappserver2.Config.static_files', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("^$").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python_config', full_name='apphosting.tools.devappserver2.Config.python_config', index=9,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='php_config', full_name='apphosting.tools.devappserver2.Config.php_config', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_config', full_name='apphosting.tools.devappserver2.Config.node_config', index=11,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='java_config', full_name='apphosting.tools.devappserver2.Config.java_config', index=12,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='apphosting.tools.devappserver2.Config.custom_config', index=13,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='go_config', full_name='apphosting.tools.devappserver2.Config.go_config', index=14,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environ', full_name='apphosting.tools.devappserver2.Config.environ', index=15,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_sql_config', full_name='apphosting.tools.devappserver2.Config.cloud_sql_config', index=16,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datacenter', full_name='apphosting.tools.devappserver2.Config.datacenter', index=17,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='apphosting.tools.devappserver2.Config.instance_id', index=18,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr_log_level', full_name='apphosting.tools.devappserver2.Config.stderr_log_level', index=19,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_domain', full_name='apphosting.tools.devappserver2.Config.auth_domain', index=20,
      number=16, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_instances', full_name='apphosting.tools.devappserver2.Config.max_instances', index=21,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vm_config', full_name='apphosting.tools.devappserver2.Config.vm_config', index=22,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_port', full_name='apphosting.tools.devappserver2.Config.server_port', index=23,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vm', full_name='apphosting.tools.devappserver2.Config.vm', index=24,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grpc_apis', full_name='apphosting.tools.devappserver2.Config.grpc_apis', index=25,
      number=24, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=1094,
)


_PHPCONFIG = _descriptor.Descriptor(
  name='PhpConfig',
  full_name='apphosting.tools.devappserver2.PhpConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='php_executable_path', full_name='apphosting.tools.devappserver2.PhpConfig.php_executable_path', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_debugger', full_name='apphosting.tools.devappserver2.PhpConfig.enable_debugger', index=1,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gae_extension_path', full_name='apphosting.tools.devappserver2.PhpConfig.gae_extension_path', index=2,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xdebug_extension_path', full_name='apphosting.tools.devappserver2.PhpConfig.xdebug_extension_path', index=3,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='php_version', full_name='apphosting.tools.devappserver2.PhpConfig.php_version', index=4,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1097,
  serialized_end=1242,
)


_NODECONFIG = _descriptor.Descriptor(
  name='NodeConfig',
  full_name='apphosting.tools.devappserver2.NodeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_executable_path', full_name='apphosting.tools.devappserver2.NodeConfig.node_executable_path', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1244,
  serialized_end=1286,
)


_PYTHONCONFIG = _descriptor.Descriptor(
  name='PythonConfig',
  full_name='apphosting.tools.devappserver2.PythonConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startup_script', full_name='apphosting.tools.devappserver2.PythonConfig.startup_script', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startup_args', full_name='apphosting.tools.devappserver2.PythonConfig.startup_args', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1288,
  serialized_end=1348,
)


_JAVACONFIG = _descriptor.Descriptor(
  name='JavaConfig',
  full_name='apphosting.tools.devappserver2.JavaConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jvm_args', full_name='apphosting.tools.devappserver2.JavaConfig.jvm_args', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1350,
  serialized_end=1380,
)


_GOCONFIG = _descriptor.Descriptor(
  name='GoConfig',
  full_name='apphosting.tools.devappserver2.GoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_dir', full_name='apphosting.tools.devappserver2.GoConfig.work_dir', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_watching_go_path', full_name='apphosting.tools.devappserver2.GoConfig.enable_watching_go_path', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_debugging', full_name='apphosting.tools.devappserver2.GoConfig.enable_debugging', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1382,
  serialized_end=1469,
)


_CUSTOMCONFIG = _descriptor.Descriptor(
  name='CustomConfig',
  full_name='apphosting.tools.devappserver2.CustomConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='custom_entrypoint', full_name='apphosting.tools.devappserver2.CustomConfig.custom_entrypoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='runtime', full_name='apphosting.tools.devappserver2.CustomConfig.runtime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1471,
  serialized_end=1529,
)


_CLOUDSQL = _descriptor.Descriptor(
  name='CloudSQL',
  full_name='apphosting.tools.devappserver2.CloudSQL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mysql_host', full_name='apphosting.tools.devappserver2.CloudSQL.mysql_host', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mysql_port', full_name='apphosting.tools.devappserver2.CloudSQL.mysql_port', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mysql_user', full_name='apphosting.tools.devappserver2.CloudSQL.mysql_user', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mysql_password', full_name='apphosting.tools.devappserver2.CloudSQL.mysql_password', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mysql_socket', full_name='apphosting.tools.devappserver2.CloudSQL.mysql_socket', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1531,
  serialized_end=1647,
)


_LIBRARY = _descriptor.Descriptor(
  name='Library',
  full_name='apphosting.tools.devappserver2.Library',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apphosting.tools.devappserver2.Library.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='apphosting.tools.devappserver2.Library.version', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1649,
  serialized_end=1689,
)


_ENVIRON = _descriptor.Descriptor(
  name='Environ',
  full_name='apphosting.tools.devappserver2.Environ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='apphosting.tools.devappserver2.Environ.key', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='apphosting.tools.devappserver2.Environ.value', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1691,
  serialized_end=1728,
)


_VMCONFIG = _descriptor.Descriptor(
  name='VMConfig',
  full_name='apphosting.tools.devappserver2.VMConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='docker_daemon_url', full_name='apphosting.tools.devappserver2.VMConfig.docker_daemon_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_logs', full_name='apphosting.tools.devappserver2.VMConfig.enable_logs', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1730,
  serialized_end=1788,
)

_CONFIG.fields_by_name['libraries'].message_type = _LIBRARY
_CONFIG.fields_by_name['python_config'].message_type = _PYTHONCONFIG
_CONFIG.fields_by_name['php_config'].message_type = _PHPCONFIG
_CONFIG.fields_by_name['node_config'].message_type = _NODECONFIG
_CONFIG.fields_by_name['java_config'].message_type = _JAVACONFIG
_CONFIG.fields_by_name['custom_config'].message_type = _CUSTOMCONFIG
_CONFIG.fields_by_name['go_config'].message_type = _GOCONFIG
_CONFIG.fields_by_name['environ'].message_type = _ENVIRON
_CONFIG.fields_by_name['cloud_sql_config'].message_type = _CLOUDSQL
_CONFIG.fields_by_name['vm_config'].message_type = _VMCONFIG
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['PhpConfig'] = _PHPCONFIG
DESCRIPTOR.message_types_by_name['NodeConfig'] = _NODECONFIG
DESCRIPTOR.message_types_by_name['PythonConfig'] = _PYTHONCONFIG
DESCRIPTOR.message_types_by_name['JavaConfig'] = _JAVACONFIG
DESCRIPTOR.message_types_by_name['GoConfig'] = _GOCONFIG
DESCRIPTOR.message_types_by_name['CustomConfig'] = _CUSTOMCONFIG
DESCRIPTOR.message_types_by_name['CloudSQL'] = _CLOUDSQL
DESCRIPTOR.message_types_by_name['Library'] = _LIBRARY
DESCRIPTOR.message_types_by_name['Environ'] = _ENVIRON
DESCRIPTOR.message_types_by_name['VMConfig'] = _VMCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.Config)
  ))
_sym_db.RegisterMessage(Config)

PhpConfig = _reflection.GeneratedProtocolMessageType('PhpConfig', (_message.Message,), dict(
  DESCRIPTOR = _PHPCONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.PhpConfig)
  ))
_sym_db.RegisterMessage(PhpConfig)

NodeConfig = _reflection.GeneratedProtocolMessageType('NodeConfig', (_message.Message,), dict(
  DESCRIPTOR = _NODECONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.NodeConfig)
  ))
_sym_db.RegisterMessage(NodeConfig)

PythonConfig = _reflection.GeneratedProtocolMessageType('PythonConfig', (_message.Message,), dict(
  DESCRIPTOR = _PYTHONCONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.PythonConfig)
  ))
_sym_db.RegisterMessage(PythonConfig)

JavaConfig = _reflection.GeneratedProtocolMessageType('JavaConfig', (_message.Message,), dict(
  DESCRIPTOR = _JAVACONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.JavaConfig)
  ))
_sym_db.RegisterMessage(JavaConfig)

GoConfig = _reflection.GeneratedProtocolMessageType('GoConfig', (_message.Message,), dict(
  DESCRIPTOR = _GOCONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.GoConfig)
  ))
_sym_db.RegisterMessage(GoConfig)

CustomConfig = _reflection.GeneratedProtocolMessageType('CustomConfig', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMCONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.CustomConfig)
  ))
_sym_db.RegisterMessage(CustomConfig)

CloudSQL = _reflection.GeneratedProtocolMessageType('CloudSQL', (_message.Message,), dict(
  DESCRIPTOR = _CLOUDSQL,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.CloudSQL)
  ))
_sym_db.RegisterMessage(CloudSQL)

Library = _reflection.GeneratedProtocolMessageType('Library', (_message.Message,), dict(
  DESCRIPTOR = _LIBRARY,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.Library)
  ))
_sym_db.RegisterMessage(Library)

Environ = _reflection.GeneratedProtocolMessageType('Environ', (_message.Message,), dict(
  DESCRIPTOR = _ENVIRON,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.Environ)
  ))
_sym_db.RegisterMessage(Environ)

VMConfig = _reflection.GeneratedProtocolMessageType('VMConfig', (_message.Message,), dict(
  DESCRIPTOR = _VMCONFIG,
  __module__ = 'google.appengine.tools.devappserver2.runtime_config_pb2'
  # @@protoc_insertion_point(class_scope:apphosting.tools.devappserver2.VMConfig)
  ))
_sym_db.RegisterMessage(VMConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

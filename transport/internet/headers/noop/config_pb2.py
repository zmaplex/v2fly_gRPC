# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/noop/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/headers/noop/config.proto',
  package='v2ray.core.transport.internet.headers.noop',
  syntax='proto3',
  serialized_options=b'\n.com.v2ray.core.transport.internet.headers.noopP\001Z>github.com/v2fly/v2ray-core/v4/transport/internet/headers/noop\252\002*V2Ray.Core.Transport.Internet.Headers.Noop',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,transport/internet/headers/noop/config.proto\x12*v2ray.core.transport.internet.headers.noop\"\x08\n\x06\x43onfig\"\x12\n\x10\x43onnectionConfigB\x9f\x01\n.com.v2ray.core.transport.internet.headers.noopP\x01Z>github.com/v2fly/v2ray-core/v4/transport/internet/headers/noop\xaa\x02*V2Ray.Core.Transport.Internet.Headers.Noopb\x06proto3'
)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.headers.noop.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=100,
)


_CONNECTIONCONFIG = _descriptor.Descriptor(
  name='ConnectionConfig',
  full_name='v2ray.core.transport.internet.headers.noop.ConnectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['ConnectionConfig'] = _CONNECTIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.headers.noop.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.headers.noop.Config)
  })
_sym_db.RegisterMessage(Config)

ConnectionConfig = _reflection.GeneratedProtocolMessageType('ConnectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONCONFIG,
  '__module__' : 'transport.internet.headers.noop.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.headers.noop.ConnectionConfig)
  })
_sym_db.RegisterMessage(ConnectionConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

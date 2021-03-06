# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/grpc/encoding/stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/grpc/encoding/stream.proto',
  package='v2ray.core.transport.internet.grpc.encoding',
  syntax='proto3',
  serialized_options=b'Z?github.com/v2fly/v2ray-core/v4/transport/internet/grpc/encoding',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-transport/internet/grpc/encoding/stream.proto\x12+v2ray.core.transport.internet.grpc.encoding\"\x14\n\x04Hunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32}\n\nGunService\x12o\n\x03Tun\x12\x31.v2ray.core.transport.internet.grpc.encoding.Hunk\x1a\x31.v2ray.core.transport.internet.grpc.encoding.Hunk(\x01\x30\x01\x42\x41Z?github.com/v2fly/v2ray-core/v4/transport/internet/grpc/encodingb\x06proto3'
)




_HUNK = _descriptor.Descriptor(
  name='Hunk',
  full_name='v2ray.core.transport.internet.grpc.encoding.Hunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='v2ray.core.transport.internet.grpc.encoding.Hunk.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=94,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['Hunk'] = _HUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hunk = _reflection.GeneratedProtocolMessageType('Hunk', (_message.Message,), {
  'DESCRIPTOR' : _HUNK,
  '__module__' : 'transport.internet.grpc.encoding.stream_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.grpc.encoding.Hunk)
  })
_sym_db.RegisterMessage(Hunk)


DESCRIPTOR._options = None

_GUNSERVICE = _descriptor.ServiceDescriptor(
  name='GunService',
  full_name='v2ray.core.transport.internet.grpc.encoding.GunService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=116,
  serialized_end=241,
  methods=[
  _descriptor.MethodDescriptor(
    name='Tun',
    full_name='v2ray.core.transport.internet.grpc.encoding.GunService.Tun',
    index=0,
    containing_service=None,
    input_type=_HUNK,
    output_type=_HUNK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GUNSERVICE)

DESCRIPTOR.services_by_name['GunService'] = _GUNSERVICE

# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/tls/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/headers/tls/config.proto',
  package='v2ray.core.transport.internet.headers.tls',
  syntax='proto3',
  serialized_options=b'\n-com.v2ray.core.transport.internet.headers.tlsP\001Z=github.com/v2fly/v2ray-core/v4/transport/internet/headers/tls\252\002)V2Ray.Core.Transport.Internet.Headers.Tls',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+transport/internet/headers/tls/config.proto\x12)v2ray.core.transport.internet.headers.tls\"\x0e\n\x0cPacketConfigB\x9c\x01\n-com.v2ray.core.transport.internet.headers.tlsP\x01Z=github.com/v2fly/v2ray-core/v4/transport/internet/headers/tls\xaa\x02)V2Ray.Core.Transport.Internet.Headers.Tlsb\x06proto3'
)




_PACKETCONFIG = _descriptor.Descriptor(
  name='PacketConfig',
  full_name='v2ray.core.transport.internet.headers.tls.PacketConfig',
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
  serialized_start=90,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['PacketConfig'] = _PACKETCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketConfig = _reflection.GeneratedProtocolMessageType('PacketConfig', (_message.Message,), {
  'DESCRIPTOR' : _PACKETCONFIG,
  '__module__' : 'transport.internet.headers.tls.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.headers.tls.PacketConfig)
  })
_sym_db.RegisterMessage(PacketConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
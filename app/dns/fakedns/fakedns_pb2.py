# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/dns/fakedns/fakedns.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/dns/fakedns/fakedns.proto',
  package='v2ray.core.app.dns.fakedns',
  syntax='proto3',
  serialized_options=b'\n\036com.v2ray.core.app.dns.fakednsP\001Z.github.com/v2fly/v2ray-core/v4/app/dns/fakedns\252\002\032V2Ray.Core.App.Dns.Fakedns',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x61pp/dns/fakedns/fakedns.proto\x12\x1av2ray.core.app.dns.fakedns\"/\n\x0b\x46\x61keDnsPool\x12\x0f\n\x07ip_pool\x18\x01 \x01(\t\x12\x0f\n\x07lruSize\x18\x02 \x01(\x03\"J\n\x10\x46\x61keDnsPoolMulti\x12\x36\n\x05pools\x18\x01 \x03(\x0b\x32\'.v2ray.core.app.dns.fakedns.FakeDnsPoolBo\n\x1e\x63om.v2ray.core.app.dns.fakednsP\x01Z.github.com/v2fly/v2ray-core/v4/app/dns/fakedns\xaa\x02\x1aV2Ray.Core.App.Dns.Fakednsb\x06proto3'
)




_FAKEDNSPOOL = _descriptor.Descriptor(
  name='FakeDnsPool',
  full_name='v2ray.core.app.dns.fakedns.FakeDnsPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_pool', full_name='v2ray.core.app.dns.fakedns.FakeDnsPool.ip_pool', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lruSize', full_name='v2ray.core.app.dns.fakedns.FakeDnsPool.lruSize', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=61,
  serialized_end=108,
)


_FAKEDNSPOOLMULTI = _descriptor.Descriptor(
  name='FakeDnsPoolMulti',
  full_name='v2ray.core.app.dns.fakedns.FakeDnsPoolMulti',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pools', full_name='v2ray.core.app.dns.fakedns.FakeDnsPoolMulti.pools', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=110,
  serialized_end=184,
)

_FAKEDNSPOOLMULTI.fields_by_name['pools'].message_type = _FAKEDNSPOOL
DESCRIPTOR.message_types_by_name['FakeDnsPool'] = _FAKEDNSPOOL
DESCRIPTOR.message_types_by_name['FakeDnsPoolMulti'] = _FAKEDNSPOOLMULTI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FakeDnsPool = _reflection.GeneratedProtocolMessageType('FakeDnsPool', (_message.Message,), {
  'DESCRIPTOR' : _FAKEDNSPOOL,
  '__module__' : 'app.dns.fakedns.fakedns_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.dns.fakedns.FakeDnsPool)
  })
_sym_db.RegisterMessage(FakeDnsPool)

FakeDnsPoolMulti = _reflection.GeneratedProtocolMessageType('FakeDnsPoolMulti', (_message.Message,), {
  'DESCRIPTOR' : _FAKEDNSPOOLMULTI,
  '__module__' : 'app.dns.fakedns.fakedns_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.app.dns.fakedns.FakeDnsPoolMulti)
  })
_sym_db.RegisterMessage(FakeDnsPoolMulti)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

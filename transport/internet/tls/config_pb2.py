# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/tls/config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transport/internet/tls/config.proto',
  package='v2ray.core.transport.internet.tls',
  syntax='proto3',
  serialized_options=b'\n%com.v2ray.core.transport.internet.tlsP\001Z5github.com/v2fly/v2ray-core/v4/transport/internet/tls\252\002!V2Ray.Core.Transport.Internet.Tls',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#transport/internet/tls/config.proto\x12!v2ray.core.transport.internet.tls\"\xba\x01\n\x0b\x43\x65rtificate\x12\x13\n\x0b\x43\x65rtificate\x18\x01 \x01(\x0c\x12\x0b\n\x03Key\x18\x02 \x01(\x0c\x12\x43\n\x05usage\x18\x03 \x01(\x0e\x32\x34.v2ray.core.transport.internet.tls.Certificate.Usage\"D\n\x05Usage\x12\x10\n\x0c\x45NCIPHERMENT\x10\x00\x12\x14\n\x10\x41UTHORITY_VERIFY\x10\x01\x12\x13\n\x0f\x41UTHORITY_ISSUE\x10\x02\"\xd1\x01\n\x06\x43onfig\x12\x16\n\x0e\x61llow_insecure\x18\x01 \x01(\x08\x12\x43\n\x0b\x63\x65rtificate\x18\x02 \x03(\x0b\x32..v2ray.core.transport.internet.tls.Certificate\x12\x13\n\x0bserver_name\x18\x03 \x01(\t\x12\x15\n\rnext_protocol\x18\x04 \x03(\t\x12!\n\x19\x65nable_session_resumption\x18\x05 \x01(\x08\x12\x1b\n\x13\x64isable_system_root\x18\x06 \x01(\x08\x42\x84\x01\n%com.v2ray.core.transport.internet.tlsP\x01Z5github.com/v2fly/v2ray-core/v4/transport/internet/tls\xaa\x02!V2Ray.Core.Transport.Internet.Tlsb\x06proto3'
)



_CERTIFICATE_USAGE = _descriptor.EnumDescriptor(
  name='Usage',
  full_name='v2ray.core.transport.internet.tls.Certificate.Usage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENCIPHERMENT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORITY_VERIFY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTHORITY_ISSUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=193,
  serialized_end=261,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATE_USAGE)


_CERTIFICATE = _descriptor.Descriptor(
  name='Certificate',
  full_name='v2ray.core.transport.internet.tls.Certificate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Certificate', full_name='v2ray.core.transport.internet.tls.Certificate.Certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Key', full_name='v2ray.core.transport.internet.tls.Certificate.Key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usage', full_name='v2ray.core.transport.internet.tls.Certificate.usage', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CERTIFICATE_USAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=261,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.transport.internet.tls.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_insecure', full_name='v2ray.core.transport.internet.tls.Config.allow_insecure', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='certificate', full_name='v2ray.core.transport.internet.tls.Config.certificate', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_name', full_name='v2ray.core.transport.internet.tls.Config.server_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_protocol', full_name='v2ray.core.transport.internet.tls.Config.next_protocol', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_session_resumption', full_name='v2ray.core.transport.internet.tls.Config.enable_session_resumption', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disable_system_root', full_name='v2ray.core.transport.internet.tls.Config.disable_system_root', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=264,
  serialized_end=473,
)

_CERTIFICATE.fields_by_name['usage'].enum_type = _CERTIFICATE_USAGE
_CERTIFICATE_USAGE.containing_type = _CERTIFICATE
_CONFIG.fields_by_name['certificate'].message_type = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Certificate'] = _CERTIFICATE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Certificate = _reflection.GeneratedProtocolMessageType('Certificate', (_message.Message,), {
  'DESCRIPTOR' : _CERTIFICATE,
  '__module__' : 'transport.internet.tls.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.tls.Certificate)
  })
_sym_db.RegisterMessage(Certificate)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'transport.internet.tls.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.transport.internet.tls.Config)
  })
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

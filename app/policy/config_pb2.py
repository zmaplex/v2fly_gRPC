# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/policy/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.protoext import extensions_pb2 as common_dot_protoext_dot_extensions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pp/policy/config.proto\x12\x15v2ray.core.app.policy\x1a common/protoext/extensions.proto\"\x17\n\x06Second\x12\r\n\x05value\x18\x01 \x01(\r\"\xdd\x03\n\x06Policy\x12\x36\n\x07timeout\x18\x01 \x01(\x0b\x32%.v2ray.core.app.policy.Policy.Timeout\x12\x32\n\x05stats\x18\x02 \x01(\x0b\x32#.v2ray.core.app.policy.Policy.Stats\x12\x34\n\x06\x62uffer\x18\x03 \x01(\x0b\x32$.v2ray.core.app.policy.Policy.Buffer\x1a\xdd\x01\n\x07Timeout\x12\x30\n\thandshake\x18\x01 \x01(\x0b\x32\x1d.v2ray.core.app.policy.Second\x12\x36\n\x0f\x63onnection_idle\x18\x02 \x01(\x0b\x32\x1d.v2ray.core.app.policy.Second\x12\x32\n\x0buplink_only\x18\x03 \x01(\x0b\x32\x1d.v2ray.core.app.policy.Second\x12\x34\n\rdownlink_only\x18\x04 \x01(\x0b\x32\x1d.v2ray.core.app.policy.Second\x1a\x33\n\x05Stats\x12\x13\n\x0buser_uplink\x18\x01 \x01(\x08\x12\x15\n\ruser_downlink\x18\x02 \x01(\x08\x1a\x1c\n\x06\x42uffer\x12\x12\n\nconnection\x18\x01 \x01(\x05\"\xb7\x01\n\x0cSystemPolicy\x12\x38\n\x05stats\x18\x01 \x01(\x0b\x32).v2ray.core.app.policy.SystemPolicy.Stats\x1am\n\x05Stats\x12\x16\n\x0einbound_uplink\x18\x01 \x01(\x08\x12\x18\n\x10inbound_downlink\x18\x02 \x01(\x08\x12\x17\n\x0foutbound_uplink\x18\x03 \x01(\x08\x12\x19\n\x11outbound_downlink\x18\x04 \x01(\x08\"\xde\x01\n\x06\x43onfig\x12\x37\n\x05level\x18\x01 \x03(\x0b\x32(.v2ray.core.app.policy.Config.LevelEntry\x12\x33\n\x06system\x18\x02 \x01(\x0b\x32#.v2ray.core.app.policy.SystemPolicy\x1aK\n\nLevelEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.v2ray.core.app.policy.Policy:\x02\x38\x01:\x19\x82\xb5\x18\t\n\x07service\x82\xb5\x18\x08\x12\x06policyB`\n\x19\x63om.v2ray.core.app.policyP\x01Z)github.com/v2fly/v2ray-core/v5/app/policy\xaa\x02\x15V2Ray.Core.App.Policyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'app.policy.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.v2ray.core.app.policyP\001Z)github.com/v2fly/v2ray-core/v5/app/policy\252\002\025V2Ray.Core.App.Policy'
  _CONFIG_LEVELENTRY._options = None
  _CONFIG_LEVELENTRY._serialized_options = b'8\001'
  _CONFIG._options = None
  _CONFIG._serialized_options = b'\202\265\030\t\n\007service\202\265\030\010\022\006policy'
  _SECOND._serialized_start=84
  _SECOND._serialized_end=107
  _POLICY._serialized_start=110
  _POLICY._serialized_end=587
  _POLICY_TIMEOUT._serialized_start=283
  _POLICY_TIMEOUT._serialized_end=504
  _POLICY_STATS._serialized_start=506
  _POLICY_STATS._serialized_end=557
  _POLICY_BUFFER._serialized_start=559
  _POLICY_BUFFER._serialized_end=587
  _SYSTEMPOLICY._serialized_start=590
  _SYSTEMPOLICY._serialized_end=773
  _SYSTEMPOLICY_STATS._serialized_start=664
  _SYSTEMPOLICY_STATS._serialized_end=773
  _CONFIG._serialized_start=776
  _CONFIG._serialized_end=998
  _CONFIG_LEVELENTRY._serialized_start=896
  _CONFIG_LEVELENTRY._serialized_end=971
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: message_broker.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'message_broker.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14message_broker.proto\x12\rmessagebroker\"+\n\x07Message\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"!\n\x0e\x43hannelRequest\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\x98\x01\n\rMessageBroker\x12;\n\x0bSendMessage\x12\x16.messagebroker.Message\x1a\x14.messagebroker.Empty\x12J\n\x0fReceiveMessages\x12\x1d.messagebroker.ChannelRequest\x1a\x16.messagebroker.Message0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_broker_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MESSAGE']._serialized_start=39
  _globals['_MESSAGE']._serialized_end=82
  _globals['_CHANNELREQUEST']._serialized_start=84
  _globals['_CHANNELREQUEST']._serialized_end=117
  _globals['_EMPTY']._serialized_start=119
  _globals['_EMPTY']._serialized_end=126
  _globals['_MESSAGEBROKER']._serialized_start=129
  _globals['_MESSAGEBROKER']._serialized_end=281
# @@protoc_insertion_point(module_scope)

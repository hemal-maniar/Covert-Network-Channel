# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msgdef.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='msgdef.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmsgdef.proto\"3\n\x12\x45xpressionResponse\x12\x0f\n\x07\x65ncrypt\x18\x01 \x01(\x0c\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\x62\x06proto3'
)




_EXPRESSIONRESPONSE = _descriptor.Descriptor(
  name='ExpressionResponse',
  full_name='ExpressionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='encrypt', full_name='ExpressionResponse.encrypt', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='ExpressionResponse.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=16,
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['ExpressionResponse'] = _EXPRESSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExpressionResponse = _reflection.GeneratedProtocolMessageType('ExpressionResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPRESSIONRESPONSE,
  '__module__' : 'msgdef_pb2'
  # @@protoc_insertion_point(class_scope:ExpressionResponse)
  })
_sym_db.RegisterMessage(ExpressionResponse)


# @@protoc_insertion_point(module_scope)

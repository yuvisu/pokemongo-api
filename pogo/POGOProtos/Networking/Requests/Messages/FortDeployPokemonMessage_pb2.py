# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/FortDeployPokemonMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/FortDeployPokemonMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nFPOGOProtos/Networking/Requests/Messages/FortDeployPokemonMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\"r\n\x18\x46ortDeployPokemonMessage\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x12\n\npokemon_id\x18\x02 \x01(\x06\x12\x17\n\x0fplayer_latitude\x18\x03 \x01(\x01\x12\x18\n\x10player_longitude\x18\x04 \x01(\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FORTDEPLOYPOKEMONMESSAGE = _descriptor.Descriptor(
  name='FortDeployPokemonMessage',
  full_name='POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage.pokemon_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_latitude', full_name='POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage.player_latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_longitude', full_name='POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage.player_longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['FortDeployPokemonMessage'] = _FORTDEPLOYPOKEMONMESSAGE

FortDeployPokemonMessage = _reflection.GeneratedProtocolMessageType('FortDeployPokemonMessage', (_message.Message,), dict(
  DESCRIPTOR = _FORTDEPLOYPOKEMONMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.FortDeployPokemonMessage)
  ))
_sym_db.RegisterMessage(FortDeployPokemonMessage)


# @@protoc_insertion_point(module_scope)

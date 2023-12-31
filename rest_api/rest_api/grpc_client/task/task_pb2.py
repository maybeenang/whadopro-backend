# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntask.proto\x12\x04task\"z\n\x04Task\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x12\n\nproject_id\x18\x06 \x01(\x05\x12\x10\n\x08user_ids\x18\x07 \x03(\x05\"\x11\n\x0fTaskListRequest\"-\n\x10TaskListResponse\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.task.Task\"\x19\n\x0bTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x0cTaskResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.task.Task\"{\n\x11TaskCreateRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x12\n\nproject_id\x18\x05 \x01(\x05\x12\x10\n\x08user_ids\x18\x06 \x03(\x05\".\n\x12TaskCreateResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.task.Task\"s\n\x11TaskUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x10\n\x08user_ids\x18\x06 \x03(\x05\".\n\x12TaskUpdateResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.task.Task\"\x1f\n\x11TaskDeleteRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x14\n\x12TaskDeleteResponse\"5\n\x17TaskUpdateStatusRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"4\n\x18TaskUpdateStatusResponse\x12\x18\n\x04task\x18\x01 \x01(\x0b\x32\n.task.Task\"-\n\x17TaskGetByProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\x05\"5\n\x18TaskGetByProjectResponse\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.task.Task\"\'\n\x14TaskGetByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"2\n\x15TaskGetByUserResponse\x12\x19\n\x05tasks\x18\x01 \x03(\x0b\x32\n.task.Task2\x8d\x04\n\x0bTaskService\x12\x35\n\x04List\x12\x15.task.TaskListRequest\x1a\x16.task.TaskListResponse\x12,\n\x03Get\x12\x11.task.TaskRequest\x1a\x12.task.TaskResponse\x12;\n\x06\x43reate\x12\x17.task.TaskCreateRequest\x1a\x18.task.TaskCreateResponse\x12;\n\x06Update\x12\x17.task.TaskUpdateRequest\x1a\x18.task.TaskUpdateResponse\x12;\n\x06\x44\x65lete\x12\x17.task.TaskDeleteRequest\x1a\x18.task.TaskDeleteResponse\x12M\n\x0cUpdateStatus\x12\x1d.task.TaskUpdateStatusRequest\x1a\x1e.task.TaskUpdateStatusResponse\x12M\n\x0cGetByProject\x12\x1d.task.TaskGetByProjectRequest\x1a\x1e.task.TaskGetByProjectResponse\x12\x44\n\tGetByUser\x12\x1a.task.TaskGetByUserRequest\x1a\x1b.task.TaskGetByUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'task_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TASK']._serialized_start=20
  _globals['_TASK']._serialized_end=142
  _globals['_TASKLISTREQUEST']._serialized_start=144
  _globals['_TASKLISTREQUEST']._serialized_end=161
  _globals['_TASKLISTRESPONSE']._serialized_start=163
  _globals['_TASKLISTRESPONSE']._serialized_end=208
  _globals['_TASKREQUEST']._serialized_start=210
  _globals['_TASKREQUEST']._serialized_end=235
  _globals['_TASKRESPONSE']._serialized_start=237
  _globals['_TASKRESPONSE']._serialized_end=277
  _globals['_TASKCREATEREQUEST']._serialized_start=279
  _globals['_TASKCREATEREQUEST']._serialized_end=402
  _globals['_TASKCREATERESPONSE']._serialized_start=404
  _globals['_TASKCREATERESPONSE']._serialized_end=450
  _globals['_TASKUPDATEREQUEST']._serialized_start=452
  _globals['_TASKUPDATEREQUEST']._serialized_end=567
  _globals['_TASKUPDATERESPONSE']._serialized_start=569
  _globals['_TASKUPDATERESPONSE']._serialized_end=615
  _globals['_TASKDELETEREQUEST']._serialized_start=617
  _globals['_TASKDELETEREQUEST']._serialized_end=648
  _globals['_TASKDELETERESPONSE']._serialized_start=650
  _globals['_TASKDELETERESPONSE']._serialized_end=670
  _globals['_TASKUPDATESTATUSREQUEST']._serialized_start=672
  _globals['_TASKUPDATESTATUSREQUEST']._serialized_end=725
  _globals['_TASKUPDATESTATUSRESPONSE']._serialized_start=727
  _globals['_TASKUPDATESTATUSRESPONSE']._serialized_end=779
  _globals['_TASKGETBYPROJECTREQUEST']._serialized_start=781
  _globals['_TASKGETBYPROJECTREQUEST']._serialized_end=826
  _globals['_TASKGETBYPROJECTRESPONSE']._serialized_start=828
  _globals['_TASKGETBYPROJECTRESPONSE']._serialized_end=881
  _globals['_TASKGETBYUSERREQUEST']._serialized_start=883
  _globals['_TASKGETBYUSERREQUEST']._serialized_end=922
  _globals['_TASKGETBYUSERRESPONSE']._serialized_start=924
  _globals['_TASKGETBYUSERRESPONSE']._serialized_end=974
  _globals['_TASKSERVICE']._serialized_start=977
  _globals['_TASKSERVICE']._serialized_end=1502
# @@protoc_insertion_point(module_scope)

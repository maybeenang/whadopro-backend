# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import task_pb2 as task__pb2


class TaskServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/task.TaskService/List',
                request_serializer=task__pb2.TaskListRequest.SerializeToString,
                response_deserializer=task__pb2.TaskListResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/task.TaskService/Get',
                request_serializer=task__pb2.TaskRequest.SerializeToString,
                response_deserializer=task__pb2.TaskResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/task.TaskService/Create',
                request_serializer=task__pb2.TaskCreateRequest.SerializeToString,
                response_deserializer=task__pb2.TaskCreateResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/task.TaskService/Update',
                request_serializer=task__pb2.TaskUpdateRequest.SerializeToString,
                response_deserializer=task__pb2.TaskUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/task.TaskService/Delete',
                request_serializer=task__pb2.TaskDeleteRequest.SerializeToString,
                response_deserializer=task__pb2.TaskDeleteResponse.FromString,
                )
        self.UpdateStatus = channel.unary_unary(
                '/task.TaskService/UpdateStatus',
                request_serializer=task__pb2.TaskUpdateStatusRequest.SerializeToString,
                response_deserializer=task__pb2.TaskUpdateStatusResponse.FromString,
                )
        self.GetByProject = channel.unary_unary(
                '/task.TaskService/GetByProject',
                request_serializer=task__pb2.TaskGetByProjectRequest.SerializeToString,
                response_deserializer=task__pb2.TaskGetByProjectResponse.FromString,
                )
        self.GetByUser = channel.unary_unary(
                '/task.TaskService/GetByUser',
                request_serializer=task__pb2.TaskGetByUserRequest.SerializeToString,
                response_deserializer=task__pb2.TaskGetByUserResponse.FromString,
                )


class TaskServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetByUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=task__pb2.TaskListRequest.FromString,
                    response_serializer=task__pb2.TaskListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=task__pb2.TaskRequest.FromString,
                    response_serializer=task__pb2.TaskResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=task__pb2.TaskCreateRequest.FromString,
                    response_serializer=task__pb2.TaskCreateResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=task__pb2.TaskUpdateRequest.FromString,
                    response_serializer=task__pb2.TaskUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=task__pb2.TaskDeleteRequest.FromString,
                    response_serializer=task__pb2.TaskDeleteResponse.SerializeToString,
            ),
            'UpdateStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStatus,
                    request_deserializer=task__pb2.TaskUpdateStatusRequest.FromString,
                    response_serializer=task__pb2.TaskUpdateStatusResponse.SerializeToString,
            ),
            'GetByProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByProject,
                    request_deserializer=task__pb2.TaskGetByProjectRequest.FromString,
                    response_serializer=task__pb2.TaskGetByProjectResponse.SerializeToString,
            ),
            'GetByUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetByUser,
                    request_deserializer=task__pb2.TaskGetByUserRequest.FromString,
                    response_serializer=task__pb2.TaskGetByUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'task.TaskService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TaskService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/List',
            task__pb2.TaskListRequest.SerializeToString,
            task__pb2.TaskListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/Get',
            task__pb2.TaskRequest.SerializeToString,
            task__pb2.TaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/Create',
            task__pb2.TaskCreateRequest.SerializeToString,
            task__pb2.TaskCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/Update',
            task__pb2.TaskUpdateRequest.SerializeToString,
            task__pb2.TaskUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/Delete',
            task__pb2.TaskDeleteRequest.SerializeToString,
            task__pb2.TaskDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/UpdateStatus',
            task__pb2.TaskUpdateStatusRequest.SerializeToString,
            task__pb2.TaskUpdateStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/GetByProject',
            task__pb2.TaskGetByProjectRequest.SerializeToString,
            task__pb2.TaskGetByProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetByUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/task.TaskService/GetByUser',
            task__pb2.TaskGetByUserRequest.SerializeToString,
            task__pb2.TaskGetByUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

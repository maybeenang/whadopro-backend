# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import project_pb2 as project__pb2


class ProjectServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/project.ProjectService/List',
                request_serializer=project__pb2.ProjectListRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectListResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/project.ProjectService/Get',
                request_serializer=project__pb2.ProjectGetRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/project.ProjectService/Create',
                request_serializer=project__pb2.ProjectCreateRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectCreateResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/project.ProjectService/Update',
                request_serializer=project__pb2.ProjectUpdateRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/project.ProjectService/Delete',
                request_serializer=project__pb2.ProjectDeleteRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectDeleteResponse.FromString,
                )
        self.AddTask = channel.unary_unary(
                '/project.ProjectService/AddTask',
                request_serializer=project__pb2.ProjectAddTaskRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectAddTaskResponse.FromString,
                )
        self.RemoveTask = channel.unary_unary(
                '/project.ProjectService/RemoveTask',
                request_serializer=project__pb2.ProjectRemoveTaskRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectRemoveTaskResponse.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/project.ProjectService/AddUser',
                request_serializer=project__pb2.ProjectAddUserRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectAddUserResponse.FromString,
                )
        self.RemoveUser = channel.unary_unary(
                '/project.ProjectService/RemoveUser',
                request_serializer=project__pb2.ProjectRemoveUserRequest.SerializeToString,
                response_deserializer=project__pb2.ProjectRemoveUserResponse.FromString,
                )
        self.GenerateLink = channel.unary_unary(
                '/project.ProjectService/GenerateLink',
                request_serializer=project__pb2.GenerateLinkProjectRequest.SerializeToString,
                response_deserializer=project__pb2.GenerateLinkProjectResponse.FromString,
                )


class ProjectServiceServicer(object):
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

    def AddTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateLink(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=project__pb2.ProjectListRequest.FromString,
                    response_serializer=project__pb2.ProjectListResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=project__pb2.ProjectGetRequest.FromString,
                    response_serializer=project__pb2.ProjectResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=project__pb2.ProjectCreateRequest.FromString,
                    response_serializer=project__pb2.ProjectCreateResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=project__pb2.ProjectUpdateRequest.FromString,
                    response_serializer=project__pb2.ProjectUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=project__pb2.ProjectDeleteRequest.FromString,
                    response_serializer=project__pb2.ProjectDeleteResponse.SerializeToString,
            ),
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=project__pb2.ProjectAddTaskRequest.FromString,
                    response_serializer=project__pb2.ProjectAddTaskResponse.SerializeToString,
            ),
            'RemoveTask': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveTask,
                    request_deserializer=project__pb2.ProjectRemoveTaskRequest.FromString,
                    response_serializer=project__pb2.ProjectRemoveTaskResponse.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=project__pb2.ProjectAddUserRequest.FromString,
                    response_serializer=project__pb2.ProjectAddUserResponse.SerializeToString,
            ),
            'RemoveUser': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUser,
                    request_deserializer=project__pb2.ProjectRemoveUserRequest.FromString,
                    response_serializer=project__pb2.ProjectRemoveUserResponse.SerializeToString,
            ),
            'GenerateLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateLink,
                    request_deserializer=project__pb2.GenerateLinkProjectRequest.FromString,
                    response_serializer=project__pb2.GenerateLinkProjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'project.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
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
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/List',
            project__pb2.ProjectListRequest.SerializeToString,
            project__pb2.ProjectListResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/Get',
            project__pb2.ProjectGetRequest.SerializeToString,
            project__pb2.ProjectResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/Create',
            project__pb2.ProjectCreateRequest.SerializeToString,
            project__pb2.ProjectCreateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/Update',
            project__pb2.ProjectUpdateRequest.SerializeToString,
            project__pb2.ProjectUpdateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/Delete',
            project__pb2.ProjectDeleteRequest.SerializeToString,
            project__pb2.ProjectDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/AddTask',
            project__pb2.ProjectAddTaskRequest.SerializeToString,
            project__pb2.ProjectAddTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/RemoveTask',
            project__pb2.ProjectRemoveTaskRequest.SerializeToString,
            project__pb2.ProjectRemoveTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/AddUser',
            project__pb2.ProjectAddUserRequest.SerializeToString,
            project__pb2.ProjectAddUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/RemoveUser',
            project__pb2.ProjectRemoveUserRequest.SerializeToString,
            project__pb2.ProjectRemoveUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectService/GenerateLink',
            project__pb2.GenerateLinkProjectRequest.SerializeToString,
            project__pb2.GenerateLinkProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

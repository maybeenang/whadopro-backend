# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

# import rest_api.grpc_client.member_pb2 as member__pb2

import rest_api.grpc_client.member.member_pb2 as member__pb2


class MemberServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
            "/member.MemberService/List",
            request_serializer=member__pb2.MemberListRequest.SerializeToString,
            response_deserializer=member__pb2.MemberListResponse.FromString,
        )
        self.Get = channel.unary_unary(
            "/member.MemberService/Get",
            request_serializer=member__pb2.MemberGetRequest.SerializeToString,
            response_deserializer=member__pb2.MemberGetResponse.FromString,
        )
        self.Create = channel.unary_unary(
            "/member.MemberService/Create",
            request_serializer=member__pb2.MemberCreateRequest.SerializeToString,
            response_deserializer=member__pb2.MemberCreateResponse.FromString,
        )
        self.Update = channel.unary_unary(
            "/member.MemberService/Update",
            request_serializer=member__pb2.MemberUpdateRequest.SerializeToString,
            response_deserializer=member__pb2.MemberUpdateResponse.FromString,
        )
        self.Delete = channel.unary_unary(
            "/member.MemberService/Delete",
            request_serializer=member__pb2.MemberDeleteRequest.SerializeToString,
            response_deserializer=member__pb2.MemberDeleteResponse.FromString,
        )


class MemberServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MemberServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "List": grpc.unary_unary_rpc_method_handler(
            servicer.List,
            request_deserializer=member__pb2.MemberListRequest.FromString,
            response_serializer=member__pb2.MemberListResponse.SerializeToString,
        ),
        "Get": grpc.unary_unary_rpc_method_handler(
            servicer.Get,
            request_deserializer=member__pb2.MemberGetRequest.FromString,
            response_serializer=member__pb2.MemberGetResponse.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=member__pb2.MemberCreateRequest.FromString,
            response_serializer=member__pb2.MemberCreateResponse.SerializeToString,
        ),
        "Update": grpc.unary_unary_rpc_method_handler(
            servicer.Update,
            request_deserializer=member__pb2.MemberUpdateRequest.FromString,
            response_serializer=member__pb2.MemberUpdateResponse.SerializeToString,
        ),
        "Delete": grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=member__pb2.MemberDeleteRequest.FromString,
            response_serializer=member__pb2.MemberDeleteResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "member.MemberService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MemberService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/member.MemberService/List",
            member__pb2.MemberListRequest.SerializeToString,
            member__pb2.MemberListResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Get(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/member.MemberService/Get",
            member__pb2.MemberGetRequest.SerializeToString,
            member__pb2.MemberGetResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Create(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/member.MemberService/Create",
            member__pb2.MemberCreateRequest.SerializeToString,
            member__pb2.MemberCreateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Update(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/member.MemberService/Update",
            member__pb2.MemberUpdateRequest.SerializeToString,
            member__pb2.MemberUpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Delete(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/member.MemberService/Delete",
            member__pb2.MemberDeleteRequest.SerializeToString,
            member__pb2.MemberDeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
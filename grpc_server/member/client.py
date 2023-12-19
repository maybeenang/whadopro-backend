import grpc
import member_pb2
import member_pb2_grpc


class MemberClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5002

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        # bind the client and the server
        self.stub = member_pb2_grpc.MemberServiceStub(self.channel)

    def getMember(self, id):
        try:
            # create a valid request message
            member_request = member_pb2.MemberGetRequest(id=id)

            # make the call
            member_response = self.stub.Get(member_request)

            return dict(
                status=True,
                id=member_response.id,
                name=member_response.name,
                email=member_response.email,
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def getAllMember(self):
        try:
            # create a valid request message
            member_request = member_pb2.MemberListRequest()

            # make the call
            member_response = self.stub.List(member_request)

            return [
                dict(
                    id=member.id,
                    name=member.name,
                    email=member.email,
                )
                for member in member_response.members
            ]

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def updateMember(self, id, name, email):
        try:
            # create a valid request message
            member_request = member_pb2.MemberUpdateRequest(
                member=member_pb2.Member(id=id, name=name, email=email)
            )

            # make the call
            member_response = self.stub.Update(member_request)

            return dict(
                status=True,
                id=member_response.member.id,
                name=member_response.member.name,
                email=member_response.member.email,
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())


if __name__ == "__main__":
    client = MemberClient()
    # respone = client.getMember(1)
    # respone = client.getAllMember()
    respone = client.updateMember(1, "test", "test@gmail.com")
    print(respone)

import rest_api.grpc_client.user.user_pb2_grpc as pb2_grpc
import rest_api.grpc_client.user.user_pb2 as pb2
import grpc


class UserClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5001

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        # bind the client and the server
        self.stub = pb2_grpc.UserServiceStub(self.channel)

    def login(self, email, password):
        try:
            # create a valid request message
            request = pb2.LoginRequest(email=email, password=password)
            # make the call
            response = self.stub.Login(request)

            return dict(
                status=True,
                token=response.token,
                id=response.id,
                name=response.name,
                email=response.email,
            )
        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def register(self, name, email, password):
        try:
            # create a valid request message
            request = pb2.RegisterRequest(name=name, email=email, password=password)
            # make the call
            response = self.stub.Register(request)

            return dict(
                status=True,
                name=response.name,
                email=response.email,
            )
        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def logout(self, email):
        try:
            # create a valid request message
            request = pb2.LogoutRequest(
                email=email,
            )
            # make the call
            response = self.stub.Logout(request)

            return dict(
                status=True,
                message=response.message,
            )
        except grpc.RpcError as e:
            return dict(status=False, message=e.details())


# if __name__ == "__main__":
# client = UserClient()
# response = client.login("maybeenang@dev.com", "12345678")
# response = client.register("maybeenang2", "maybeenang2@dev.com", "12345678")
# response = client.logout("maybeenang@dev.com")
# print(response)

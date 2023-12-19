from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest_api.grpc_client.user.user_client import UserClient


@view_defaults(renderer="json")
class UserController:
    def __init__(self, request):
        self.request = request

    @view_config(route_name="login", request_method="POST")
    def login(self):
        try:
            if (
                "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            email = self.request.json_body["email"]
            password = self.request.json_body["password"]

            client = UserClient()
            response = client.login(email, password)

            if response == None:
                return Response(
                    status=401,
                    json_body=dict(
                        status=False,
                        message="Unauthorized",
                    ),
                )

            if response["status"]:
                return response

            return Response(
                status=401,
                json_body=dict(
                    status=False,
                    message=response["message"],
                ),
            )

        except Exception as e:
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

    @view_config(route_name="register", request_method="POST")
    def register(self):
        try:
            if (
                "name" not in self.request.json_body
                or "email" not in self.request.json_body
                or "password" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            name = self.request.json_body["name"]
            email = self.request.json_body["email"]
            password = self.request.json_body["password"]

            client = UserClient()
            response = client.register(name, email, password)

            if response["status"]:
                return response

            return Response(
                status=401,
                json_body=dict(
                    status=False,
                    message=response["message"],
                ),
            )

        except Exception as e:
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

    @view_config(route_name="logout", request_method="POST")
    def logout(self):
        try:
            if "email" not in self.request.json_body:
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            email = self.request.json_body["email"]

            client = UserClient()
            response = client.logout(email)

            if response["status"]:
                return response

            return Response(
                status=401,
                json_body=dict(
                    status=False,
                    message=response["message"],
                ),
            )

        except Exception as e:
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest_api.grpc_client.project.project_client import ProjectClient

import traceback


@view_defaults(route_name="project", renderer="json")
class ProjectController:
    def __init__(self, request):
        self.request = request

    @view_config(request_method="GET", route_name="project_user_id")
    def getProject(self):
        try:
            if self.request.params.get("id") is None:
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )
            id = self.request.params.get("id")

            client = ProjectClient()
            response = client.getProject(int(id))

            return Response(
                json_body=dict(
                    response,
                ),
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

    @view_config(request_method="POST")
    def create(self):
        try:
            if (
                "title" not in self.request.json_body
                or "description" not in self.request.json_body
                or "user_id" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            title = self.request.json_body["title"]
            description = self.request.json_body["description"]
            user_id = self.request.json_body["user_id"]

            client = ProjectClient()
            response = client.createProject(
                title=title,
                description=description,
                user_id=user_id,
            )

            if response is not None:
                return Response(
                    json_body=dict(
                        response,
                    ),
                )

            return Response(
                status=401,
                json_body=dict(
                    status=False,
                    message=response,
                ),
            )

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

    @view_config(request_method="GET")
    def getProjectByUserId(self):
        try:
            if self.request.params.get("userId") is None:
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            user_id = self.request.params.get("userId")

            client = ProjectClient()
            response = client.getProjectByUserId(int(user_id))

            if (type(response) is list) and (len(response) > 0):
                return response

            if response["status"] == False:
                return Response(
                    status=404,
                    json_body=dict(
                        status=False,
                        message=response["message"],
                    ),
                )

            return response

        except Exception as e:
            print(e)
            return Response(
                status=500,
                json_body=dict(
                    status=False,
                    message="Internal Server Error",
                ),
            )

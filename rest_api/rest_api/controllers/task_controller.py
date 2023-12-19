from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest_api.grpc_client.task.task_client import TaskClient
import traceback


@view_defaults(route_name="task", renderer="json")
class TaskController:
    def __init__(self, request):
        self.request = request

    @view_config(
        request_method="POST", route_name="update_task_status", renderer="json"
    )
    def updateStatus(self):
        print("updateStatus")
        try:
            if (
                "id" not in self.request.json_body
                or "status" not in self.request.json_body
            ):
                return Response(
                    status=400,
                    json_body=dict(
                        status=False,
                        message="Bad Request",
                    ),
                )

            id = self.request.json_body["id"]
            status = self.request.json_body["status"]

            client = TaskClient()
            response = client.updateTaskStatus(
                id=int(id),
                status=status,
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

    @view_config(request_method="POST")
    def createTask(self):
        try:
            if (
                "title" not in self.request.json_body
                or "description" not in self.request.json_body
                or "status" not in self.request.json_body
                or "date" not in self.request.json_body
                or "project_id" not in self.request.json_body
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
            status = self.request.json_body["status"]
            date = self.request.json_body["date"]
            project_id = self.request.json_body["project_id"]

            client = TaskClient()
            response = client.createTask(
                title=title,
                description=description,
                status=status,
                date=date,
                project_id=int(project_id),
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

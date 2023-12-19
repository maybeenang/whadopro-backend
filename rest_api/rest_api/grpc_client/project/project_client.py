import rest_api.grpc_client.project.project_pb2_grpc as pb2_grpc
import rest_api.grpc_client.project.project_pb2 as pb2
import grpc

from rest_api.grpc_client.task.task_client import TaskClient


class ProjectClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5003

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        # bind the client and the server
        self.stub = pb2_grpc.ProjectServiceStub(self.channel)

    def getAllProject(self):
        try:
            # create a valid request message
            project_request = pb2.ProjectListRequest()

            # make the call
            project_response = self.stub.List(project_request)

            return [
                dict(
                    id=project.id,
                    title=project.title,
                    description=project.description,
                    user_id=project.user_id,
                )
                for project in project_response.projects
            ]

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def getProject(self, id):
        try:
            # create a valid request message
            project_request = pb2.ProjectGetRequest(id=id)

            # make the call
            project_response = self.stub.Get(project_request)

            task_client = TaskClient()

            return dict(
                id=project_response.project.id,
                title=project_response.project.title,
                description=project_response.project.description,
                user_id=project_response.project.user_id,
                tasks=task_client.getTaskByProjectId(project_response.project.id),
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def createProject(self, title, description, user_id):
        try:
            # create a valid request message
            project_request = pb2.ProjectCreateRequest(
                description=description,
                title=title,
                user_id=user_id,
            )

            # make the call
            project_response = self.stub.Create(project_request)

            return dict(
                title=project_response.project.title,
                description=project_response.project.description,
                user_id=project_response.project.user_id,
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def getProjectByUserId(self, user_id):
        try:
            # create a valid request message
            project_request = pb2.GetProjectByUserIdRequest(user_id=user_id)

            # make the call
            project_response = self.stub.GetByUserId(project_request)

            task_client = TaskClient()

            return [
                dict(
                    id=project.id,
                    title=project.title,
                    description=project.description,
                    user_id=project.user_id,
                    tasks=task_client.getTaskByProjectId(project.id),
                )
                for project in project_response.projects
            ]

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())


# if __name__ == "__main__":
#     client = ProjectClient()
#     # res = client.getAllProject()
#     # res = client.getProject(1)
#     # res = client.createProject("title", "description", 1)
#     res = client.getProjectByUserId(2)
#     print(res)

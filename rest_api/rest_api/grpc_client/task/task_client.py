import rest_api.grpc_client.task.task_pb2_grpc as pb2_grpc
import rest_api.grpc_client.task.task_pb2 as pb2
import grpc


class TaskClient:
    def __init__(self):
        self.host = "localhost"
        self.server_port = 5004

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.server_port)
        )

        # bind the client and the server
        self.stub = pb2_grpc.TaskServiceStub(self.channel)

    def getTaskByProjectId(self, project_id):
        try:
            # create a valid request message
            task_request = pb2.TaskGetByProjectRequest(project_id=project_id)

            # make the call
            task_response = self.stub.GetByProject(task_request)

            return [
                dict(
                    id=task.id,
                    title=task.title,
                    description=task.description,
                    project_id=task.project_id,
                    status=task.status,
                    date=task.date,
                )
                for task in task_response.tasks
            ]

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def createTask(self, title, description, project_id, date, status):
        try:
            # create a valid request message
            task_request = pb2.TaskCreateRequest(
                title=title,
                description=description,
                project_id=project_id,
                date=date,
                status=status,
            )

            # make the call
            task_response = self.stub.Create(task_request)

            return dict(
                title=task_response.task.title,
                description=task_response.task.description,
                project_id=task_response.task.project_id,
                date=task_response.task.date,
                status=task_response.task.status,
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())

    def updateTaskStatus(self, id, status):
        try:
            # create a valid request message
            task_request = pb2.TaskUpdateStatusRequest(
                id=id,
                status=status,
            )

            # make the call
            task_response = self.stub.UpdateStatus(task_request)

            return dict(
                title=task_response.task.title,
                description=task_response.task.description,
                project_id=task_response.task.project_id,
                date=task_response.task.date,
                status=task_response.task.status,
            )

        except grpc.RpcError as e:
            return dict(status=False, message=e.details())


if __name__ == "__main__":
    client = TaskClient()
    # res = client.getTaskByProjectId(1)
    # res = client.createTask("title", "description", 1, "2021-01-01", "todo")
    res = client.updateTaskStatus(1, "review")
    print(res)

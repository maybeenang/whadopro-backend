from concurrent import futures
import time
import logging
import grpc

import traceback

import jwt

from database.config import engine

from model.task import Task
from sqlalchemy import insert, text, values, select, update, delete, desc

import task_pb2
import task_pb2_grpc


class TaskServicer(task_pb2_grpc.TaskServiceServicer):
    def GetByProject(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Task).where(Task.project_id == request.project_id)
                ).fetchall()

                conn.commit()

                tasks = []
                for row in res:
                    tasks.append(
                        task_pb2.Task(
                            id=row.id,
                            title=row.title,
                            description=row.description,
                            project_id=row.project_id,
                        )
                    )

                return task_pb2.TaskListResponse(tasks=tasks)
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return task_pb2.TaskListResponse()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                conn.execute(
                    insert(Task).values(
                        title=request.title,
                        description=request.description,
                        project_id=request.project_id,
                        date=request.date,
                        status=request.status,
                    )
                )

                conn.commit()

                return task_pb2.TaskCreateResponse(
                    task=task_pb2.Task(
                        title=request.title,
                        description=request.description,
                        project_id=request.project_id,
                        date=request.date,
                        status=request.status,
                    ),
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return task_pb2.TaskCreateResponse()

    def UpdateStatus(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Task).where(Task.id == request.id)).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Task not found!")
                    return task_pb2.Task()

                conn.execute(
                    update(Task)
                    .where(Task.id == request.id)
                    .values(
                        status=request.status,
                    )
                )

                conn.commit()

                return task_pb2.TaskUpdateStatusResponse(
                    task=task_pb2.Task(
                        title=res.title,
                        description=res.description,
                        project_id=res.project_id,
                        date=res.date,
                        status=request.status,
                    ),
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return task_pb2.TaskUpdateStatusResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_TaskServiceServicer_to_server(TaskServicer(), server)
    server.add_insecure_port("localhost:5004")
    server.start()
    print("Server started at localhost:5004")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

from concurrent import futures
import time
import logging
import grpc

import traceback

import jwt

from database.config import engine

from model.project import Project
from sqlalchemy import insert, text, values, select, update, delete, desc


import project_pb2
import project_pb2_grpc


class ProjectServicer(project_pb2_grpc.ProjectServiceServicer):
    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Project)).fetchall()

                conn.commit()

                projects = []
                for row in res:
                    projects.append(
                        project_pb2.Project(
                            id=row.id,
                            title=row.title,
                            description=row.description,
                            user_id=row.user_id,
                        )
                    )

                return project_pb2.ProjectListResponse(projects=projects)
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return project_pb2.ProjectListResponse()

    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Project).where(Project.id == request.id)
                ).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Project not found!")
                    return project_pb2.Project()

                return project_pb2.ProjectResponse(
                    project=project_pb2.Project(
                        id=res.id,
                        title=res.title,
                        description=res.description,
                        user_id=res.user_id,
                    )
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return project_pb2.Project()

    def Create(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                conn.execute(
                    insert(Project).values(
                        title=request.title,
                        description=request.description,
                        user_id=request.user_id,
                    )
                )

                conn.commit()

                return project_pb2.ProjectCreateResponse(
                    project=project_pb2.Project(
                        title=request.title,
                        description=request.description,
                        user_id=request.user_id,
                    )
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return project_pb2.Project()

    def GetByUserId(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Project).where(Project.user_id == request.user_id)
                ).fetchall()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Project not found!")
                    return project_pb2.Project()

                projects = []
                for row in res:
                    projects.append(
                        project_pb2.Project(
                            id=row.id,
                            title=row.title,
                            description=row.description,
                            user_id=row.user_id,
                        )
                    )

                return project_pb2.ProjectListResponse(projects=projects)
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return project_pb2.ProjectListResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    project_pb2_grpc.add_ProjectServiceServicer_to_server(ProjectServicer(), server)
    server.add_insecure_port("localhost:5003")
    server.start()
    print("Server started at localhost:5003")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

from concurrent import futures
import time
import logging
import grpc

import traceback

import jwt

from database.config import engine

from model.member import Member
from sqlalchemy import insert, text, values, select, update, delete, desc


import user_pb2
import user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServiceServicer):
    def Login(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Member).where(Member.email == request.email)
                ).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Email not found!")
                    return user_pb2.LoginResponse()

                if res.password != request.password:
                    context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                    context.set_details("Password incorrect!")
                    return user_pb2.LoginResponse()

                    # generate token
                token = jwt.encode(
                    {"email": request.email, "nama": res[1]},
                    "secret",
                    algorithm="HS256",
                )

                # update token
                conn.execute(
                    update(Member)
                    .where(Member.email == request.email)
                    .values(token=token)
                )

                conn.commit()

                context.set_code(grpc.StatusCode.OK)
                context.set_details("Login success!")

                return user_pb2.LoginResponse(
                    email=res.email,
                    name=res.name,
                    id=res.id,
                    token=token,
                )

        except Exception as e:
            logging.error(traceback.format_exc())
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Internal error!")
            raise e

    def Register(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Member).where(Member.email == request.email)
                ).fetchone()

                if res is not None:
                    context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                    context.set_details("Email already exists!")
                    return user_pb2.RegisterResponse()

                conn.execute(
                    insert(Member).values(
                        name=request.name,
                        email=request.email,
                        password=request.password,
                    )
                )

                conn.commit()

                context.set_code(grpc.StatusCode.OK)
                context.set_details("Register success!")

                return user_pb2.RegisterResponse(
                    email=request.email,
                    name=request.name,
                )

        except Exception as e:
            logging.error(traceback.format_exc())
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Internal error!")
            raise e

    def Logout(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Member).where(Member.email == request.email)
                ).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Email not found!")
                    return user_pb2.LogoutResponse()

                # update token
                conn.execute(
                    update(Member).where(Member.email == request.email).values(token="")
                )

                conn.commit()

                context.set_code(grpc.StatusCode.OK)
                context.set_details("Logout success!")

                return user_pb2.LogoutResponse(
                    message="Logout success!",
                )

        except Exception as e:
            logging.error(traceback.format_exc())
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Internal error!")
            raise e


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServicer(), server)
    server.add_insecure_port("localhost:5001")
    server.start()
    print("Server started at localhost:5001")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

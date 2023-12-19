from concurrent import futures
import time
import logging
import grpc

import traceback

import jwt

from database.config import engine

from model.member import Member
from sqlalchemy import insert, text, values, select, update, delete, desc


import member_pb2
import member_pb2_grpc


class MemberServicer(member_pb2_grpc.MemberServiceServicer):
    def Get(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Member).where(Member.id == request.id)
                ).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Member not found!")
                    return member_pb2.Member()

                return member_pb2.MemberGetResponse(
                    email=res.email,
                    name=res.name,
                    id=res.id,
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return member_pb2.Member()

    def List(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(select(Member)).fetchall()

                conn.commit()

                members = []
                for row in res:
                    members.append(
                        member_pb2.Member(
                            id=row.id,
                            name=row.name,
                            email=row.email,
                        )
                    )
                return member_pb2.MemberListResponse(
                    members=members,
                )
        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return member_pb2.Members()

    def Update(self, request, context):
        try:
            with engine.connect() as conn:
                conn.begin()

                res = conn.execute(
                    select(Member).where(Member.id == request.member.id)
                ).fetchone()

                if res is None:
                    context.set_code(grpc.StatusCode.NOT_FOUND)
                    context.set_details("Member not found!")
                    return member_pb2.Member()

                conn.execute(
                    update(Member)
                    .where(Member.id == request.member.id)
                    .values(
                        name=request.member.name,
                        email=request.member.email,
                    )
                )

                conn.commit()

                return member_pb2.MemberUpdateResponse(
                    member=member_pb2.Member(
                        id=request.member.id,
                        name=request.member.name,
                        email=request.member.email,
                    )
                )

        except Exception as e:
            print(traceback.format_exc())
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return member_pb2.Member()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    member_pb2_grpc.add_MemberServiceServicer_to_server(MemberServicer(), server)
    server.add_insecure_port("localhost:5002")
    server.start()
    print("Server started at localhost:5002")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

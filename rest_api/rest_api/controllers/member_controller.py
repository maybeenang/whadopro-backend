from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from rest_api.grpc_client.member.member_client import MemberClient

import traceback


@view_defaults(renderer="json")
class MemberController:
    def __init__(self, request):
        self.request = request

    @view_config(route_name="member", request_method="GET")
    def getMember(self):
        try:
            client = MemberClient()
            response = client.getAllMember()

            if response is not None:
                return Response(json_body=response)

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

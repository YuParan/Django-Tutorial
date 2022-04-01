import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from api.response import NamelessServer_Response

logger = logging.getLogger(__name__)


class JsonAPI(APIView):
    """ Postman 을 활용해서 테스트를 진행할 경우, POST Request 전송방식을 Body ~ raw(type=json) 으로 지정해줘야 합니다 """
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        :action:
            Django 에서 POST(json) Request 와 그 처리를 위한 예시 API 입니다.
            application/json (raw) 형식으로 parameter 를 입력받아 내용을 파싱한 후, json 포맷으로 동일하게 응답합니다.
        :param: request parameter
            "param0": (bool)
            "param1": (int)
            "param2": (float)
            "param3": (str)
            "param4": (dict)
            "param5": (list)
            "session": (str) 선택 파라미터 - default: "test_session"

                Test Json Raw
                {
                    "param0": false,
                    "param1": 5,
                    "param2": 2.4,
                    "param3": "flask",
                    "param4": {
                        "arg1": 1,
                        "arg2": 2
                    },
                    "param5": [9, 8.8, {"s": 7}],
                    "session": "test_session"
                }
        :return: response payload
            request parameter 와 동일한 값을 동일하게 응답합니다.
            "param0": (bool)
            "param1": (int)
            "param2": (float)
            "param3": (str)
            "param4": (dict)
            "param5": (list)
            "session": (str) 선택 파라미터 - default: "test_session"
        """
        args = dict()
        args["param0"] = request.data.get("param0")
        args["param1"] = request.data.get("param1")
        args["param2"] = request.data.get("param2")
        args["param3"] = request.data.get("param3")
        args["param4"] = request.data.get("param4")
        args["param5"] = request.data.get("param5")
        args["session"] = request.data.get("session", "test_session")

        # 필수 Parameter Check
        required_parameters = ['param0', 'param1', 'param2', 'param3', 'param4', 'param5']
        if any(args[rq] is None for rq in required_parameters):
            logger.error(args)
            return NamelessServer_Response(
                400,
                "파라미터가 존재하지 않습니다",
                {}
            )

        # 최종 정상 응답
        return NamelessServer_Response(
            200,
            "파라미터를 정상적으로 파싱하였습니다.",
            {"args": args}
        )

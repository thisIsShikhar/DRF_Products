from rest_framework.response import Response
from rest_framework.views import exception_handler


class Msg():

    @staticmethod    
    def encode(code, msg, errors, data) -> dict:
        code_to_msg = {
            200: 'Success',
            201: 'New Entry Created',
            400: 'Error',
            401: 'Unauthorized',
            403: 'Forbidden',
            404: 'Not Found'
        }
        return {
            "code": code,
            "message": msg if msg is not None else code_to_msg.get(code, f'Wrong Code {code}'),
            "errors": [] if errors is None else [f"{k}, {v[-1]}" for k, v in errors.items()],
            "data": data
        }


def custom_error(exc, context) -> Response:
    response = exception_handler(exc, context)
    try:
        msg = Msg.encode(200, None, None, response.data)
    except:
        msg = Msg.encode(400, None, {"details": "something went wrong"}, None)
    return Response(msg)
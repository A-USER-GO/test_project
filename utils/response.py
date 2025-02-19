from django.http import JsonResponse


def json_success_resp(data):
    resp = {
        'code': 0,
        'msg': 'success',
        'data': data
    }

    return JsonResponse(resp, safe=False)


def json_fail_resp(code, msg, data=None):
    resp = {
        'code': code,
        'msg': msg,
        'data': data
    }

    return JsonResponse(resp, safe=False)

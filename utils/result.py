from flask import json, Response


def build_api_result(code, message, data=None):
    """
    生成 API 请求的返回值
    :param code: 0/-1，区分成功和失败
    :param message: 返回的消息
    :param data: 返回的数据
    :return:
    """
    result = {'code': code, 'message': message}
    if data is not None:
        result['data'] = data
    json_data = json.dumps(result, ensure_ascii=False)  # 设置 ensure_ascii 为 False
    return Response(json_data, content_type='application/json; charset=utf-8')


def build_success(message, data=None):
    return build_api_result(0, message, data)


def build_error(message, data=None):
    return build_api_result(-1, message, data)

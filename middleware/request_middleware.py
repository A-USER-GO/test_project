import datetime
import json


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # 处理请求的下一步（视图）

    def __call__(self, request):
        start_time = datetime.datetime.now()  # 记录请求开始时间
        response = self.get_response(request)  # 继续处理请求
        end_time = datetime.datetime.now()  # 记录请求结束时间

        duration = (end_time - start_time).total_seconds()
        json_data = json.loads(request.body.decode('utf-8')) if request.body else {}

        # 这里可以把他修改为用log去记录，正式就应该用log
        print(f"请求 {request.path} GET参数: {request.GET} POST参数：{request.POST} json参数：{json_data} 处理时间: {duration} 秒")

        return response  # 返回响应




from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 如下，等于'*'后，便可允许所有简单请求的跨域访问
        response['Access-Control-Allow-Origin'] = '*'
        # 判断是否为复杂请求
        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Access-Control-Allow-Methods'] = 'PUT,PATCH,DELETE'

        return response

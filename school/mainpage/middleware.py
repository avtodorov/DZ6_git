import time
import re

from mainpage.models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        path = request.path
        method = request.method
        epoch = time.time()

        response = self.get_response(request)

        estimation = round((time.time() - epoch) * 1000, 2)

        if '/admin/' in path:
            Logger.objects.create(method=method, path=path, execution_time=estimation)

        return response

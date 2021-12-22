# import time
#
#
# class RequestLoggerMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         """
#         Code to be executed for each request before the view (and later
#         middleware) are called.
#         """
#         epoch = time.time()
#
#         response = self.get_response(request)
#
#         estimation = round((time.time() - epoch) * 1000)
#         print(f'Estimation time {estimation} miliseconds')
#         return response

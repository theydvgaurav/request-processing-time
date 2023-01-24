from django.utils import timezone
from requestprocessingtime.colors import Colors


class ProcessingTimeMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.start_time = timezone.now()

    def process_response(self, request, response):
        total_time = timezone.now() - request.start_time
        print(Colors.GREEN, 'Time taken: {}'.format(total_time), Colors.END)

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        self.process_response(request, response)
        return response

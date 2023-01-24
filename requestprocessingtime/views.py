from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import time

class CustomView(APIView):
    def get(self,request):
        """

        Custom Logic

        """
        return Response("This is a response of get request")
    def post(self,request):
        """

        Custom Logic

        """
        time.sleep(0.7)
        return Response("This is a response of post request")   
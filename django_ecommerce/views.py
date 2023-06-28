from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login



class LogInView(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class LogOutView(APIView):
    def post(self, request, format=None):
        return Response("BAD")

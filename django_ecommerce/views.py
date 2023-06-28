from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login



class LogInView(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return Response(status=200)
        else:
            return Response({"detail": "Invalid credentials."}, status=401)


class LogOutView(APIView):
    def post(self, request, format=None):
        return Response("BAD")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout


class LogInView(APIView):
    def post(self, request, format=None):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


class LogOutView(APIView):
    def post(self, request, format=None):
        try:
            request.auth_token.delete()
        except:
            pass

        logout(request)

        return Response(status=status.HTTP_204_NO_CONTENT)

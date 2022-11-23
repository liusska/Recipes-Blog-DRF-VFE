from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer


class LeadPagination(PageNumberPagination):
    page_size = 2


class RegisterView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(
            email=email,
            password=password
        )
        if user is not None:
            print(f"Logged user: {user}")
            response = {
                "message": "Login Successful",
                "token": "Token " + user.auth_token.key,
                "user": {
                    "email": user.email,
                    "username": user.username,
                },
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={
            "message": "Invalid email or password",
        })

    def get(self, request):
        content = {
            "user": str(self.request.user),
            "auth": str(self.request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)


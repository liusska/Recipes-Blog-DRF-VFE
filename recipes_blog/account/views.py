from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignUpSerializer
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


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
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(data=content, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "User logout successfully"
        }
        return response


class UserRecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.filter(author=self.request.user.id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(data=serializer.data,  status=status.HTTP_200_OK)


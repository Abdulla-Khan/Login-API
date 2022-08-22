from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from authentication.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serilaizer = UserSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

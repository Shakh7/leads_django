from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ApiKey
from .serializers import ApiKeySerializer


class ApiKeyListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        keys = ApiKey.objects.all()
        serializer = ApiKeySerializer(keys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    # def post(self, request, *args, **kwargs):
    #     '''
    #     Create the Todo with given todo data
    #     '''
    #     data = {
    #         'task': request.data.get('task'),
    #         'completed': request.data.get('completed'),
    #         'user': request.user.id
    #     }
    #     serializer = ApiKeySerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

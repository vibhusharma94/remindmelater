# rest framework modules
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

# app level modules
from .serializer import (
    ReminderSerializer,)


class ReminderApi(generics.GenericAPIView):

    def post(self, request):
        data = request.data.copy()
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)

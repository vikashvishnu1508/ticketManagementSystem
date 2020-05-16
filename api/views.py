from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ticket.models import *
from api.serializers import IssueSerializer
# Create your views here.


class CreateIssueAPI(APIView):
    def post(self, request, format=None):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            jsonobj = serializer.data
            jsonobj['id'] = serializer.instance.pk
            return Response(jsonobj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

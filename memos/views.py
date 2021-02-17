from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import Memo
from .serializers import MemoSerializer



# Create your views here.

class MemoListAPIView(APIView):

    def get(self, request):
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MemoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)








from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


from .models import Memo
from .serializers import MemoSerializer



# Create your views here.
""" APIView fro the list of Memos """
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


class MemoDetailAPIView(APIView):

    def get_object(self, slug):
        try:
            return Memo.objects.get(slug=slug)
        except Memo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, slug):
        memo = self.get_object(slug)
        serializer = MemoSerializer(memo)
        return Response(serializer.data)

    def put(self, request, slug):
        memo = self.get_object(slug)
        serializer = MemoSerializer(memo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        memo = self.get_object(slug)
        memo.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)








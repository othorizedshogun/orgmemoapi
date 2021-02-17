from rest_framework import serializers
from .models import Memo


""" creating a serializser for the Memo Model """
class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = '__all__'


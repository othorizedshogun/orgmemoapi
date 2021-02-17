from django.urls import path
from .views import MemoListAPIView



urlpatterns = [
    path('memos/', MemoListAPIView.as_view())
]


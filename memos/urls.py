from django.urls import path
from .views import MemoListAPIView, MemoDetailAPIView



urlpatterns = [
    path('memos/', MemoListAPIView.as_view()),
    path('memos/detail/<str:slug>/', MemoDetailAPIView.as_view())
]


from django.urls import path
from . import views

urlpatterns = [
    path('api/article/', views.ArticleListCreate.as_view() ),
]
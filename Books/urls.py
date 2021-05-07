"""Books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from core import views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-tokn-auth'),

    path('user_list_create/', views.BaseUserAPIView.as_view(), name="user_list_create"),
    path('user/<int:pk>/', views.BaseUserDetailAPIView.as_view(), name="user_details"),

    path('sub_catagory_list_create/', views.SubCategoryAPIView.as_view(), name="sub_catagory_list_create"),
    path('sub_catagory/<int:pk>/', views.SubCategoryDetailAPIView.as_view(), name="sub_catagory_details"),

    path('catagory_list_create/', views.CategoryAPIView.as_view(), name="catagory_list_create"),
    path('catagory/<int:pk>/', views.CategoryDetailAPIView.as_view(), name="catagory_details"),

    path('author_list_create/', views.AuthorAPIView.as_view(), name="author_list_create"),
    path('author/<int:pk>/', views.AuthorDetailAPIView.as_view(), name="author_details"),

    path('book_list_create/', views.BookAPIView.as_view(), name="book_list_create"),
    path('book/<int:pk>/', views.BookDetailAPIView.as_view(), name="book_details"),

    path('book_return_list_create/', views.BookReturnAPIView.as_view(), name="book_return_list_create"),
    path('book_return/<int:pk>/', views.BookReturnDetailAPIView.as_view(), name="book_return_details"),

]
urlpatterns += router.urls
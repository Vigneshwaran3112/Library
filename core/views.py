from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class BaseUserAPIView(APIView):

    def get(self, request):
        serializer = BaseUserSerializer(BaseUser.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = BaseUser.objects.create(username=e['username'], user_id=e['user_id'], phone=e['phone'], is_member=e['is_member'], address=e['address'])
        serializer = BaseUserSerializer(d)
        return Response(serializer.data)


class BaseUserDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = BaseUserSerializer(BaseUser.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)


    def put(self, request, pk):
        emp = BaseUser.objects.get(pk=pk, status=True, delete=False)
        serializer = BaseUserSerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = BaseUser.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'BaseUser deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)


class SubCategoryAPIView(APIView):

    def get(self, request):
        serializer = SubCategorySerializer(SubCategory.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request, format='html'):
        e = request.data
        d = SubCategory.objects.create(name=e['name'], description=e['description'], code=e['code'])
        serializer = SubCategorySerializer(d)
        return Response(serializer.data)


class SubCategoryDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = SubCategorySerializer(SubCategory.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = SubCategory.objects.get(pk=pk, status=True, delete=False)
        serializer = SubCategorySerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = SubCategory.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'SubCategory deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)


class CategoryAPIView(APIView):

    def get(self, request):
        serializer = CategorySerializer(Category.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = Category.objects.create(name=e['name'], sub_category=e['sub_category'], description=e['description'], code=e['code'])
        serializer = CategorySerializer(d)
        return Response(serializer.data)


class CategoryDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = CategorySerializer(Category.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = Category.objects.get(pk=pk, status=True, delete=False)
        serializer = CategorySerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = Category.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'Category deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)


class AuthorAPIView(APIView):

    def get(self, request):
        serializer = AuthorSerializer(Author.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = Author.objects.create(name=e['name'], address=e['address'], dob=e['dob'], author_code=e['author_code'], description=e['description'])
        serializer = AuthorSerializer(d)
        return Response(serializer.data)


class AuthorDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = AuthorSerializer(Author.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = Author.objects.get(pk=pk, status=True, delete=False)
        serializer = AuthorSerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = Author.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'Author deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)


class BookAPIView(APIView):

    def get(self, request):
        serializer = BookSerializer(Book.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = Book.objects.create(name=e['name'], category=e['category'], pages=e['pages'], mrp_price=e['mrp_price'],
                                edition=e['edition'], publish_date=e['publish_date'], written_by=e['written_by'],
                                description=e['description'], code=e['code'])
        serializer = BookSerializer(d)
        return Response(serializer.data)


class BookDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = BookSerializer(Book.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = Book.objects.get(pk=pk, status=True, delete=False)
        serializer = BookSerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = Book.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'Book deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)


class BookReturnAPIView(APIView):

    def get(self, request):
        serializer = BookReturnSerializer(BookReturn.objects.filter(status=True, delete=False), many=True)
        return Response(serializer.data)

    def post(self, request):
        e = request.data
        d = BookReturn.objects.create(user=e['user'], book=e['book'], enter_time=e['enter_time'], leave_time=e['leave_time'])
        serializer = BookReturnSerializer(d)
        return Response(serializer.data)


class BookReturnDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            serializer = BookReturnSerializer(BookReturn.objects.get(pk=pk, status=True, delete=False))
            return Response(serializer.data)
        except:
            return Response({'message': 'Data Not Found'}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = BookReturn.objects.get(pk=pk, status=True, delete=False)
        serializer = BookReturnSerializer(emp, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        emp = BookReturn.objects.filter(pk=pk).update(status=False, delete=True)
        return Response({'message': 'BookReturn deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)




























# class SubCategoryAPIView(viewsets.ModelViewSet):
#     queryset = SubCategory.objects.filter(status=True, delete=False)
#     serializer_class = SubCategorySerializer
#
#     def destroy(self, request, *args, **kwargs):
#         destroy = SubCategory.objects.filter(pk=kwargs['pk']).update(status=False, delete=True)
#         return Response({'message': 'SubCategory deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)



# class CategoryAPIView(viewsets.ModelViewSet):
#     queryset = Category.objects.filter(status=True, delete=False)
#     serializer_class = CategorySerializer
#
#     def destroy(self, request, *args, **kwargs):
#         destroy = Category.objects.filter(pk=kwargs['pk']).update(status=False, delete=True)
#         return Response({'message': 'Categorydeleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)



# class AuthorAPIView(viewsets.ModelViewSet):
#     queryset = Author.objects.filter(status=True, delete=False)
#     serializer_class = AuthorSerializer
#
#     def destroy(self, request, *args, **kwargs):
#         destroy = Author.objects.filter(pk=kwargs['pk']).update(status=False, delete=True)
#         return Response({'message': 'Author deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)



# class BookAPIView(viewsets.ModelViewSet):
#     queryset = Book.objects.filter(status=True, delete=False)
#     serializer_class = BookSerializer
#
#     def destroy(self, request, *args, **kwargs):
#         destroy = Book.objects.filter(pk=kwargs['pk']).update(status=False, delete=True)
#         return Response({'message': 'Book deleted sucessfully'}, status=status.HTTP_204_NO_CONTENT)
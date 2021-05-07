from rest_framework import serializers

from .models import *


class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('url', 'username', 'user_id', 'phone', 'is_member', 'address')

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'username': instance.username,
            'user_id': instance.user_id,
            'phone': instance.phone,
            'is_member': instance.is_member,
            'address': instance.address,
        }



class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('url', 'name', 'description', 'code',)

    def to_representation(self, instance):
        return{
            'id': instance.pk,
            'name': instance.name,
            'description': instance.description,
            'code': instance.code,
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'sub_category', 'description', 'code',)

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'name': instance.name,
            'sub_category_id': instance.sub_category.values_list('pk', flat=True).order_by('pk'),
            'sub_category': SubCategorySerializer(instance.sub_category, many=True).data,
            'description': instance.description,
            'code': instance.code,
        }


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'name', 'description', 'author_code',)

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'name': instance.name,
            'description': instance.description,
            'author_code': instance.author_code,
        }


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'name', 'category', 'pages', 'mrp_price', 'edition', 'publish_date', 'written_by', 'description', 'code',)

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'name': instance.name,
            'category_id': instance.category.values_list('pk', flat=True).order_by('pk'),
            'category': CategorySerializer(instance.category, many=True).data,
            'written_by_id': instance.written_by.values_list('pk', flat=True).order_by('pk'),
            'written_by': AuthorSerializer(instance.written_by, many=True).data,
            'description': instance.description,
            'code': instance.code,
        }



class BookReturnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookReturn
        fields = ('url', 'user', 'book', 'enter_time', 'leave_time',)

    def to_representation(self, instance):
        return {
            'id': instance.pk,
            'user_id': instance.user.pk,
            'user': instance.user,
            'book': instance.book,
            'enter_time': instance.enter_time,
            'leave_time': instance.leave_time
        }
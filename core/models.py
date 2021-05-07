from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    delete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUser(AbstractUser):
    user_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, db_index=True, unique=True)
    is_member = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)


class SubCategory(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=50)
    sub_category = models.ManyToManyField(SubCategory, null=True, blank=True, related_name='sub_category')
    description = models.CharField(max_length=100)
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    dob = models.DateField()
    author_code = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Book(BaseModel):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='book_category')
    pages = models.PositiveIntegerField(default=0)
    mrp_price = models.PositiveIntegerField(default=0)
    edition = models.CharField(max_length=50, null=True, blank=True,)
    publish_date = models.DateTimeField()
    written_by = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='book_author')
    description = models.CharField(max_length=100)
    code = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} - {self.written_by.name}'


class BookReturn(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, null=True, blank=True, related_name='book_return_user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='user_book_name')
    enter_time = models.DateTimeField()
    leave_time = models.DateTimeField()



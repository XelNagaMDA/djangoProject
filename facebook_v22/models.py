from datetime import datetime
from uuid import uuid4

from django.db import models


# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    username = models.CharField(max_length=32, null=False, unique=True)
    password = models.TextField(null=False)
    registration_date = models.DateTimeField(default=datetime.now)

    @classmethod
    def create_user(cls, username: str, password):
        username = username.strip()
        if not username:
            raise Exception("Username cant be empty")
        if len(password) < 6:
            raise Exception('Password is too short')
        return cls.objects.create(
            username=username,
            password=password
        )

    def say_hi(self):
        print(f'User {self.username} says hi')


class Post(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    message = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post_date = models.DateTimeField(default=datetime.now)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, null=False, default=uuid4)
    message = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment_date = models.DateTimeField(default=datetime.now)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
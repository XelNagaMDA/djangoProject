from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from djangoProject.constants import DATE_TIME_FORMAT
from facebook_v22.models import User, Post


# Create your views here.

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    User.create_user(username, password)
    return Response(status=200)


@api_view(['GET'])
def all_users_view(request):
    data = []
    all_users = User.objects.all()
    for user in all_users:
        user.say_hi()
        data.append(
            dict(
                un=user.username,
                id=user.id,
                passwd=user.password,
                reg_date=user.registration_date.strftime(DATE_TIME_FORMAT)
            )
        )
    return Response(status=200, data=data)


@api_view(['GET'])
def users_restered_today(request):
    data = []
    all_users = User.objects.filter(
        registration_date__year=datetime.now().year,
        registration_date__month=datetime.now().month,
        registration_date__day=datetime.now().day,
    )
    for user in all_users:
        user.say_hi()
        data.append(
            dict(
                un=user.username,
                id=user.id,
                passwd=user.password,
                reg_date=user.registration_date.strftime(DATE_TIME_FORMAT)
            )
        )
    return Response(status=200, data=data)


@api_view(['POST'])
def regisration_one_day_sooner(request):
    user_id = request.data.get('id')
    my_user = User.objects.get(id=user_id)
    my_user.registration_date -= timedelta(days=1)
    my_user.save()
    return Response(status=200)


@api_view(['POST'])
def rename_user(request):
    user_id = request.data.get('id')
    new_name = request.data.get('new_name')
    my_user = User.objects.get(id=user_id)
    my_user.username = new_name
    my_user.save()
    return Response(status=200)


@api_view(['POST'])
def make_post(request):
    user_id = request.data.get('user_id')
    post_message = request.data.get('message')
    user = User.objects.get(id=user_id)
    my_new_post = Post(message=post_message, user=user)
    my_new_post.save()
    return Response(status=200)


@api_view(['GET'])
def list_posts(request):
    data = []
    for post in Post.objects.all():
        data.append(
            dict(
                message=post.message,
                username=post.user.username,
                post_date=post.post_date.strftime(DATE_TIME_FORMAT)
            )
        )
    return Response(status=200, data=data)


@api_view(['POST'])
def delete_user(request):
    user_id = request.data.get('id')
    user = User.objects.get(id=user_id)
    user.delete()
    return Response('User deleted successfully.', status=status.HTTP_204_NO_CONTENT)


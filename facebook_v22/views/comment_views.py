from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from facebook_v22.comment_services.comment_crud import create_comment
from facebook_v22.models import Post, User
from facebook_v22.serializers import CommentShallowSerializer


@api_view(['POST'])
def leave_comment(request):
    # Ce mesaj avem de comentariu
    message = request.data.get('message')
    # La ce postare
    post_id = request.data.get('post_id')
    # De la cine
    user_id = request.data.get('user_id')
    if not message or not post_id or not user_id:
        return Response(status=status.HTTP_417_EXPECTATION_FAILED)
    try:
        post = Post.objects.get(id=post_id)
        user = User.objects.get(id=user_id)
    except (Post.DoesNotExist, User.DoesNotExist):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    # Cream Comentariu
    # Salvam Comenariu
    new_comment = create_comment(post, user, message)
    serilaized_data = CommentShallowSerializer(new_comment).data
    return Response(data=serilaized_data, status=status.HTTP_201_CREATED)
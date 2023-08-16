from facebook_v22.models import Comment


class EmptyCommentException(Exception):
    pass


def create_comment(post, user, message):
    if not message:
        raise EmptyCommentException()
    return Comment.objects.create(
        post=post,
        user=user,
        message=message
    )
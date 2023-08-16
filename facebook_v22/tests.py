from django.db import IntegrityError
from django.test import TestCase, Client

from facebook_v22.comment_services.comment_crud import create_comment
from facebook_v22.models import User, Comment, Post


# Create your tests here.
class PostTests(TestCase):

    def test_post_creation(self):
        self.assertEquals(2, 2)

    def test_post_length(self):
        client = Client()
        user = User.objects.create(username='victor', password='123456')
        post_message = 'This message has less than 140 chars.' * 140
        response = client.post('/facebook/post/', {'user_id': user.id, 'message': post_message})
        self.assertEqual(response.status_code, 200)
        post = Post.objects.get(message=post_message)
        self.assertLessEqual(len(post.message), 140)



class UserTests(TestCase):

    def test_user_list_api(self):
        client = Client()
        response = client.get('/facebook/list/')
        self.assertEquals(response.status_code, 204)
        User.create_user('marius', 'password')
        response = client.get('/facebook/list/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.json()), 1)
        self.assertEquals(response.json()[0]['username'], 'marius')
        self.assertNotIn('password', response.json()[0])

    def test_user_creation(self):
        self.assertEquals(User.objects.count(), 0)
        User.create_user('marius', 'password')
        self.assertEquals(User.objects.count(), 1)
        User.create_user('marius2', 'password')
        self.assertEquals(User.objects.count(), 2)
        self.assertEquals(User.objects.filter(username='marius').count(), 1)

    def test_user_unique(self):
        # Testing that there can not be 2 users with same name
        self.assertEquals(User.objects.count(), 0)
        User.create_user('marius', 'password')
        self.assertEquals(User.objects.count(), 1)
        with self.assertRaises(IntegrityError):
            User.create_user('marius', 'password')

    def test_empty_name_not_allowed(self):
        self.assertEquals(User.objects.count(), 0)
        try:
            User.create_user('', 'password')
        except:
            pass
        # User is not created
        self.assertEquals(User.objects.count(), 0)

    def test_spaces_in_username_not_allowed(self):
        self.assertEquals(User.objects.count(), 0)
        try:
            User.create_user('    ', 'password')
        except:
            pass
        # User is not created
        self.assertEquals(User.objects.count(), 0)


class CommentTest(TestCase):

    def test_comment_creation(self):
        self.assertEquals(Comment.objects.count(), 0)
        with self.assertRaises(Exception):
            create_comment(None, None, 'Hello')


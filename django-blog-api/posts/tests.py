from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="A good title",
            body="Nice body content",
        )

    def test_post_model(self):
        post = Post.objects.get(pk=self.post.pk) 
        self.assertEqual(post.author.username, "testuser")
        self.assertEqual(post.title, "A good title")
        self.assertEqual(post.body, "Nice body content")
        self.assertEqual(str(post), "A good title")

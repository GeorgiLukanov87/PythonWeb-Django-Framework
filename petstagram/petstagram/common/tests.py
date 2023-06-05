from django.test import TestCase
from django.contrib.auth import get_user_model
from petstagram.photos.models import Photo
from .models import Comment, Like

UserModel = get_user_model()


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com',
        )
        self.photo = Photo.objects.create(
            photo='path/to/photo.jpg',
            user=self.user,
        )

    def test_comment_creation(self):
        comment = Comment(
            text='Test comment',
            to_photo=self.photo,
            user=self.user,
        )
        self.assertEqual(comment.text, 'Test comment')
        self.assertEqual(comment.to_photo, self.photo)
        self.assertEqual(comment.user, self.user)

    def test_comment_date_time_of_publication_auto_now_add(self):
        comment = Comment(
            text='Test comment',
            to_photo=self.photo,
            user=self.user,
        )
        comment.save()

        self.assertIsNotNone(comment.date_time_of_publication)

    def test_comment_ordering(self):
        comment1 = Comment.objects.create(
            text='Comment 1',
            to_photo=self.photo,
            user=self.user,
        )
        comment2 = Comment.objects.create(
            text='Comment 2',
            to_photo=self.photo,
            user=self.user,
        )
        comment3 = Comment.objects.create(
            text='Comment 3',
            to_photo=self.photo,
            user=self.user,
        )

        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment3)
        self.assertEqual(comments[1], comment2)
        self.assertEqual(comments[2], comment1)


class LikeModelTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com',
        )
        self.photo = Photo.objects.create(
            photo='path/to/photo.jpg',
            user=self.user,
        )

    def test_like_creation(self):
        like = Like(
            to_photo=self.photo,
            user=self.user,
        )
        self.assertEqual(like.to_photo, self.photo)
        self.assertEqual(like.user, self.user)

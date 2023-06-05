from django.core.exceptions import ValidationError
from django.test import TestCase
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from .models import Photo
from petstagram.pets.models import Pet

UserModel = get_user_model()


class PhotoModelTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com',
        )

    def test_photo_upload(self):
        photo = Photo(
            photo='path/to/photo.jpg',
            description='Test photo',
            location='Test location',
            user=self.user,
        )
        self.assertEqual(photo.photo, 'path/to/photo.jpg')
        self.assertEqual(photo.description, 'Test photo')
        self.assertEqual(photo.location, 'Test location')
        self.assertEqual(photo.user, self.user)

    def test_photo_description_min_length_validator(self):
        photo = Photo(
            photo='path/to/photo.jpg',
            description='Too short',
            location='Test location',
            user=self.user,
        )
        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test_photo_location_max_length_validator(self):
        photo = Photo(
            photo='path/to/photo.jpg',
            description='Test photo',
            location='a' * (Photo.PHOTO_LOCATION_MAX_LEN + 1),
            user=self.user,
        )
        with self.assertRaises(ValidationError):
            photo.full_clean()

    def test_photo_tagged_pets_relationship(self):
        pet1 = Pet.objects.create(name='Pet 1', personal_photo='http://example.com/photo1.jpg', user=self.user)
        pet2 = Pet.objects.create(name='Pet 2', personal_photo='http://example.com/photo2.jpg', user=self.user)

        photo = Photo(
            photo='path/to/photo.jpg',
            description='Test photo',
            location='Test location',
            user=self.user,
        )
        photo.save()
        photo.tagged_pets.add(pet1, pet2)

        self.assertEqual(photo.tagged_pets.count(), 2)
        self.assertIn(pet1, photo.tagged_pets.all())
        self.assertIn(pet2, photo.tagged_pets.all())

    def test_photo_date_of_publication_auto_now(self):
        photo = Photo(
            photo='path/to/photo.jpg',
            description='Test photo',
            location='Test location',
            user=self.user,
        )
        photo.save()

        self.assertIsNotNone(photo.date_of_publication)

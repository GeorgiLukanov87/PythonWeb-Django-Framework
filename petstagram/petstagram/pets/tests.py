from django.test import TestCase
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from .models import Pet

UserModel = get_user_model()


class PetModelTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com',
        )

    def test_pet_creation(self):
        pet = Pet(
            name='Fluffy',
            personal_photo='http://example.com/fluffy.jpg',
            date_of_birth='2022-01-01',
            user=self.user,
        )
        self.assertEqual(pet.name, 'Fluffy')
        self.assertEqual(pet.personal_photo, 'http://example.com/fluffy.jpg')
        self.assertEqual(pet.date_of_birth, '2022-01-01')
        self.assertEqual(pet.user, self.user)

    def test_pet_slug_creation(self):
        pet = Pet(
            name='Fluffy',
            personal_photo='http://example.com/fluffy.jpg',
            date_of_birth='2022-01-01',
            user=self.user,
        )
        pet.save()
        expected_slug = slugify(f"{pet.name}-{pet.id}")
        self.assertEqual(pet.slug, expected_slug)

    def test_pet_str_representation(self):
        pet = Pet(
            name='Fluffy',
            personal_photo='http://example.com/fluffy.jpg',
            date_of_birth='2022-01-01',
            user=self.user,
        )
        self.assertEqual(str(pet), 'Fluffy')

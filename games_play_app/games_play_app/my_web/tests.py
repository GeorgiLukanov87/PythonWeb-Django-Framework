from django.test import TestCase, Client
from django.urls import reverse
from django.core.exceptions import ValidationError

from games_play_app.my_web.forms import (
    ProfileCreateForm,
    ProfileEditForm,
    ProfileDeleteForm,
    GameCreateForm,

)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_show_index(self):
        response = self.client.get(reverse('show index'))
        self.assertEqual(response.status_code, 200)

    def test_show_dashboard(self):
        response = self.client.get(reverse('show dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_create_profile(self):
        response = self.client.get(reverse('create profile'))
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        response = self.client.get(reverse('create game'))
        self.assertEqual(response.status_code, 200)


class ModelTestCase(TestCase):
    def test_profile_model(self):
        profile = Profile(
            email='test@example.com',
            age=20,
            password='testpassword',
            first_name='John',
            last_name='Doe',
            profile_picture='https://example.com/profile.jpg',
        )
        profile.full_clean()  # Validates the model fields
        profile.save()

        # Test that the model is correctly saved and retrieved from the database
        saved_profile = Profile.objects.get(email='test@example.com')
        self.assertEqual(saved_profile, profile)

    def test_game_model(self):
        game = Game(
            title='Test Game',
            category=Game.ACTION,
            rating=4.5,
            max_level=10,
            image_url='https://example.com/game.jpg',
            summary='This is a test game.',
        )
        game.full_clean()  # Validates the model fields
        game.save()

        # Test that the model is correctly saved and retrieved from the database
        saved_game = Game.objects.get(title='Test Game')
        self.assertEqual(saved_game, game)

    def test_invalid_rating_validation(self):
        invalid_ratings = [-1.0, 0.0, 5.5, 6.0]
        for rating in invalid_ratings:
            game = Game(
                title='Invalid Rating Game',
                category=Game.ACTION,
                rating=rating,
                image_url='https://example.com/game.jpg',
            )
            with self.assertRaises(ValidationError):
                game.full_clean()

    def test_min_age_validation(self):
        invalid_ages = [0, 5, 10]
        for age in invalid_ages:
            profile = Profile(
                email='test@example.com',
                age=age,
                password='testpassword',
            )
            with self.assertRaises(ValidationError):
                profile.full_clean()


from games_play_app.my_web.models import Profile, Game


class FormTestCase(TestCase):
    def test_profile_create_form_valid(self):
        form_data = {
            'email': 'test@example.com',
            'age': 25,
            'password': 'testpassword',
        }
        form = ProfileCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_valid(self):
        profile = Profile.objects.create(
            email='test@example.com',
            age=25,
            password='testpassword',
        )
        form_data = {
            'email': 'updated@example.com',
            'age': 30,
            'password': 'updatedpassword',
        }
        form = ProfileEditForm(data=form_data, instance=profile)
        self.assertTrue(form.is_valid())

    def test_profile_delete_form_valid(self):
        profile = Profile.objects.create(
            email='test@example.com',
            age=25,
            password='testpassword',
        )
        form_data = {}
        form = ProfileDeleteForm(data=form_data, instance=profile)
        self.assertTrue(form.is_valid())

    def test_game_create_form_valid(self):
        form_data = {
            'title': 'Test Game',
            'category': Game.ACTION,
            'rating': 4.5,
            'max_level': 10,
            'image_url': 'https://example.com/game.jpg',
            'summary': 'This is a test game.',
        }
        form = GameCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

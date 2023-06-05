from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Gender, AppUser


class ChoicesEnumMixinTestCase(TestCase):
    def test_choices_method_returns_choices_list(self):
        choices = Gender.choices()
        expected_choices = [('male', 'Male'), ('female', 'Female'), ('DoNotShow', 'Do not show')]
        self.assertEqual(choices, expected_choices)

    def test_max_len_method_returns_max_length_of_choices(self):
        max_len = Gender.max_len()
        expected_max_len = max(len(name) for name, _ in Gender.choices())
        self.assertEqual(max_len, expected_max_len)


class AppUserModelTestCase(TestCase):
    def test_first_name_min_length_validator(self):
        user = AppUser(first_name='A', last_name='Smith', email='a@example.com', gender='male')
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_last_name_min_length_validator(self):
        user = AppUser(first_name='John', last_name='S', email='john@example.com', gender='male')
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_first_name_only_letters_validator(self):
        user = AppUser(first_name='John1', last_name='Smith', email='john@example.com', gender='male')
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_last_name_only_letters_validator(self):
        user = AppUser(first_name='John', last_name='Smith1', email='john@example.com', gender='male')
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_email_unique_validator(self):
        user1 = AppUser(first_name='John', last_name='Smith', email='john@example.com', gender='male')
        user1.save()
        user2 = AppUser(first_name='Jane', last_name='Doe', email='john@example.com', gender='female')
        with self.assertRaises(ValidationError):
            user2.full_clean()



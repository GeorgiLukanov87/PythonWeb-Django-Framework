from django.test import TestCase,Client

from django.core.exceptions import ValidationError
from car_collection_app.web.models import Profile, Car
from car_collection_app.web.forms import ProfileCreateForm, ProfileEditForm, ProfileDeleteForm, CarCreateForm, CarEditForm, CarDeleteForm



class ProfileModelTest(TestCase):
    def test_username_min_length(self):
        # Test that the username must have a minimum length of 2
        profile = Profile(username='a', email='test@example.com', age=20, password='password')
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
        self.assertTrue('The username must be a minimum of 2 chars' in str(context.exception))

    def test_age_validation(self):
        # Test that the age must be at least 18
        profile = Profile(username='username', email='test@example.com', age=17, password='password')
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
        self.assertTrue('You must be at least 18 years old' in str(context.exception))

    def test_valid_profile(self):
        # Test creating a valid profile
        profile = Profile(username='username', email='test@example.com', age=20, password='password')
        profile.full_clean()  # Should not raise any exceptions

class CarModelTest(TestCase):
    def test_year_validation(self):
        # Test that the year must be between 1980 and 2049
        car = Car(type='Sports Car', model='Model A', year=1970, image_url='http://example.com', price=10000)
        with self.assertRaises(ValidationError) as context:
            car.full_clean()
        self.assertTrue('Year must be between 1980 and 2049' in str(context.exception))

    def test_price_validation(self):
        # Test that the price cannot be below 1.00
        car = Car(type='Sports Car', model='Model A', year=2022, image_url='http://example.com', price=0.5)
        with self.assertRaises(ValidationError) as context:
            car.full_clean()
        self.assertTrue('Price cannot be below 1.00 $' in str(context.exception))

    def test_valid_car(self):
        # Test creating a valid car
        car = Car(type='Sports Car', model='Model A', year=2022, image_url='http://example.com', price=10000)
        car.full_clean()  # Should not raise any exceptions



class ProfileFormsTest(TestCase):
    def test_profile_create_form(self):
        form_data = {
            'username': 'username',
            'email': 'test@example.com',
            'age': 20,
            'password': 'password',
        }
        form = ProfileCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_profile_edit_form(self):
        profile = Profile.objects.create(username='username', email='test@example.com', age=20, password='password')
        form_data = {
            'username': 'new_username',
            'email': 'new_test@example.com',
            'age': 25,
            'password': 'new_password',
        }
        form = ProfileEditForm(data=form_data, instance=profile)
        self.assertTrue(form.is_valid())

    def test_profile_delete_form(self):
        profile = Profile.objects.create(username='username', email='test@example.com', age=20, password='password')
        form = ProfileDeleteForm(instance=profile)
        self.assertTrue(form.is_valid())

class CarFormsTest(TestCase):
    def test_car_create_form(self):
        form_data = {
            'type': 'Sports Car',
            'model': 'Model A',
            'year': 2022,
            'image_url': 'http://example.com',
            'price': 10000,
        }
        form = CarCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_edit_form(self):
        car = Car.objects.create(type='Sports Car', model='Model A', year=2022, image_url='http://example.com', price=10000)
        form_data = {
            'type': 'Sports Car',
            'model': 'Model B',
            'year': 2023,
            'image_url': 'http://example.com',
            'price': 15000,
        }
        form = CarEditForm(data=form_data, instance=car)
        self.assertTrue(form.is_valid())

    def test_car_delete_form(self):
        car = Car.objects.create(type='Sports Car', model='Model A', year=2022, image_url='http://example.com', price=10000)
        form = CarDeleteForm(instance=car)
        self.assertTrue(form.is_valid())

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from car_collection_app.web.views import (
    show_index, show_catalogue, create_profile, details_profile, edit_profile,
    delete_profile, create_car, details_car, edit_car, delete_car
)

class UrlsTest(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('show index')
        self.assertEqual(resolve(url).func, show_index)

    def test_catalogue_url_resolves(self):
        url = reverse('show catalogue')
        self.assertEqual(resolve(url).func, show_catalogue)

class ProfileUrlsTest(SimpleTestCase):
    def test_create_profile_url_resolves(self):
        url = reverse('create profile')
        self.assertEqual(resolve(url).func, create_profile)

    def test_details_profile_url_resolves(self):
        url = reverse('details profile')
        self.assertEqual(resolve(url).func, details_profile)

    def test_edit_profile_url_resolves(self):
        url = reverse('edit profile')
        self.assertEqual(resolve(url).func, edit_profile)

    def test_delete_profile_url_resolves(self):
        url = reverse('delete profile')
        self.assertEqual(resolve(url).func, delete_profile)

class CarUrlsTest(SimpleTestCase):
    def test_details_car_url_resolves(self):
        url = reverse('details car', args=[1])  # Replace 1 with the appropriate car ID
        self.assertEqual(resolve(url).func, details_car)

    def test_edit_car_url_resolves(self):
        url = reverse('edit car', args=[1])  # Replace 1 with the appropriate car ID
        self.assertEqual(resolve(url).func, edit_car)

    def test_delete_car_url_resolves(self):
        url = reverse('delete car', args=[1])  # Replace 1 with the appropriate car ID
        self.assertEqual(resolve(url).func, delete_car)

    def test_create_car_url_resolves(self):
        url = reverse('create car')
        self.assertEqual(resolve(url).func, create_car)


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_profile_view(self):
        url = reverse('create profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test POST request with valid data
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'age': 25,
            'password': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertEqual(Profile.objects.count(), 1)  # Verify that a profile object was created

    def test_details_profile_view(self):
        profile = Profile.objects.create(username='testuser', email='test@example.com', age=25, password='testpassword')
        url = reverse('details profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'], profile)

    # Add tests for other profile views (edit_profile, delete_profile) following a similar pattern

class CarViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_car_view(self):
        url = reverse('create car')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Test POST request with valid data
        data = {
            'type': 'Sports Car',
            'model': 'Test Model',
            'year': 2023,
            'image_url': 'http://example.com/image.jpg',
            'price': 100000.00,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertEqual(Car.objects.count(), 1)  # Verify that a car object was created

    def test_details_car_view(self):
        car = Car.objects.create(type='Sports Car', model='Test Model', year=2023, image_url='http://example.com/image.jpg', price=100000.00)
        url = reverse('details car', args=[car.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['car'], car)


from django.test import TestCase, Client
from django.urls import reverse

from online_library_app.my_web.models import Book, Profile


class ProfileModelTestCase(TestCase):
    def test_profile_model(self):
        profile = Profile.objects.create(
            first_name='John',
            last_name='Doe',
            image_url='https://example.com/image.jpg'
        )
        self.assertEqual(profile.first_name, 'John')
        self.assertEqual(profile.last_name, 'Doe')
        self.assertEqual(profile.image_url, 'https://example.com/image.jpg')
        self.assertEqual(str(profile), 'Name=John, Last name=Doe, id={}'.format(profile.id))


class BookModelTestCase(TestCase):
    def test_book_model(self):
        book = Book.objects.create(
            title='Test Book',
            description='Test description',
            image='https://example.com/book.jpg',
            type='Fiction'
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.description, 'Test description')
        self.assertEqual(book.image, 'https://example.com/book.jpg')
        self.assertEqual(book.type, 'Fiction')
        self.assertEqual(str(book), 'Book title=Test Book, id={}, type=Fiction'.format(book.id))


class MyViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(first_name='John', last_name='Doe',
                                              image_url='https://example.com/profile.jpg')
        self.book = Book.objects.create(title='Test Book', description='Test description',
                                        image='https://example.com/book.jpg', type='Fiction')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-with-profile.html')

    def test_create_profile_view(self):
        response = self.client.get(reverse('create-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/home-no-profile.html')

    def test_profile_page_view(self):
        response = self.client.get(reverse('profile-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_edit_profile_view(self):
        response = self.client.get(reverse('edit-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/edit-profile.html')

    def test_delete_profile_view(self):
        response = self.client.get(reverse('delete-profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/delete-profile.html')

    def test_add_book_view(self):
        response = self.client.get(reverse('add-book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/add-book.html')

    def test_edit_book_view(self):
        response = self.client.get(reverse('edit-book', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/edit-book.html')

    def test_details_book_view(self):
        response = self.client.get(reverse('details-book', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book-details.html')

    def test_delete_book_view(self):
        response = self.client.get(reverse('delete-book', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/delete-book.html')

    # Add more test methods for other views

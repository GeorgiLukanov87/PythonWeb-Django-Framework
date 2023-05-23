from django import forms

from online_library_app.my_web.models import Profile, Book


# Profile Forms
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name ...'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name ...',

                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image ...',
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


# Book Forms


class BookBaseForm(forms.ModelForm):
    class Meta:
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Book title ...'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'cols': 10,
                    'rows': 10,
                    'placeholder': 'Book description ...',

                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image ...',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Book Type ...'
                }
            )
        }
        model = Book
        fields = '__all__'

        labels = {
            'title': 'Book title',
            'description': 'Book description',
            'image': 'Link to image',
            'type': 'Book type',
        }


class BookCreateForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass


class BookDeleteForm(BookBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

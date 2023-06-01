from django import forms

from petstagram.common.models import Like, Comment
from petstagram.core.form_mixins import DisabledFormMixin
from petstagram.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


class PhotoDeleteForm(DisabledFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            Photo.objects.all().first().tagged_pets.clear()
            Like.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many
            Comment.objects.filter(to_photo_id=self.instance.id).delete()  # one-to-many

            self.instance.delete()

        return self.instance

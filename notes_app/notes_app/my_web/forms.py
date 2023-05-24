from django import forms

from notes_app.my_web.models import Note, Profile


# note forms
class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteEditForm(NoteBaseForm):
    pass


class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteDeleteForm(NoteBaseForm):
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


# profile forms
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass

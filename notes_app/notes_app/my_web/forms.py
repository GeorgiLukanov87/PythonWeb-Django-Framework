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


# profile forms
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass

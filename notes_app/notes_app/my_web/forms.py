from django import forms

from notes_app.my_web.models import Note


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NoteEditForm(NoteBaseForm):
    pass

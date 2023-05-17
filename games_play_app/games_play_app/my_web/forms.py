from django import forms

from games_play_app.my_web.models import Profile, Game


# PROFILE FORMS
class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "age", "password", ]
        # Password input(hidden).
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileHiddenDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class ProfileDeleteForm(ProfileHiddenDeleteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            if _ == 'password':
                # To successful delete profile , skip password input.
                continue
            field.widget.attrs['readonly'] = 'readonly'


# GAME FORMS
class GameBaseForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateForm(GameBaseForm):
    pass


class GameEditForm(GameBaseForm):
    pass


class GameDeleteForm(GameBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

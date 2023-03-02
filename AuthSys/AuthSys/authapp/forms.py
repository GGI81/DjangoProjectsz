from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth import forms as auth_forms, get_user_model

from AuthSys.authapp.models import UserProfile
from AuthSys.authapp.validators import validate_only_letters

UserModel = get_user_model()

class CreateProfileForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    first_name = forms.CharField(
        max_length=UserProfile.NAME_MAX_LEN,
        validators=(
            MinLengthValidator(UserProfile.NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    last_name = forms.CharField(
        max_length=UserProfile.NAME_MAX_LEN,
        validators=(
            MinLengthValidator(UserProfile.NAME_MIN_LEN),
            validate_only_letters,
        ),
    )

    email = forms.EmailField()


    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
        return user

    def clean_email(self):
        email_value = self.cleaned_data["email"]
        try:
            User.objects.get(username=email_value)
        except User.DoesNotExist:
            return email_value
        raise forms.ValidationError("An user with that email already exists.")


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login':
            "You have entered an invalid email or password"
        ,
        'inactive': "This account is inactive.",
    }

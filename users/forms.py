
from django import forms
from django.contrib.auth.models import User
from users.models import Profile

class ProfileForm(forms.Form):
    """Profile form."""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()


class LoginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control',
                'required': True
            }
        )
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'required': True
            }
        )
    )


class SignupForm(forms.Form):

    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder':'Username',
            'class':'form-control',
            'required': True
        })
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'placeholder':'Password',
            'class':'form-control',
            'required': True
        })
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'placeholder':'Password Confirmation',
            'class':'form-control',
            'required': True
        })
    )

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder':'Fist Name',
            'class':'form-control',
            'required': True
        })
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder':'Last Name',
            'class':'form-control',
            'required': True
        })
    )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(attrs={
            'placeholder':'email@example.com',
            'class':'form-control',
            'required': True
        })
    )

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username= username)
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError("Password and Password confirmation does't match")
        return data

    def clean_email(self):
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email)
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
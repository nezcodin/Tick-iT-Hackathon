from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-left'}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-left'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control form-left'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control form-left'}), label='Password')
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control form-left'}), label='Confirm Password')
    is_venue = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'name', 'is_venue')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name, user.last_name = self.cleaned_data['name'].split(' ', 1)
        user.save()
        return user

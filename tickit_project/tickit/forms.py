# from django import forms
# from django.contrib.auth.forms import UserCreationForm


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     name = forms.CharField(required=True)
#     options = forms.ChoiceField(choices=[('member', 'Member'), ('venue', 'Venue')])
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'email', 'name', 'options')
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.first_name, user.last_name = self.cleaned_data['name'].split(' ', 1)
#         user.save()
#         if self.cleaned_data['options'] == 'member':
#             user.is_venue = False
#         elif self.cleaned_data['options'] == 'venue':
#             user.is_venue = True
#         return user

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'name', 'is_venue')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name, user.last_name = self.cleaned_data['name'].split(' ', 1)
        user.save()
        return user

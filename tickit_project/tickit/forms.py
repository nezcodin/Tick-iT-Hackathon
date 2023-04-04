from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    options = forms.ChoiceField(choices=[('member', 'Member'), ('venue', 'Venue')], required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'name', 'options')
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name, user.last_name = self.cleaned_data['name'].split(' ', 1)
        user.save()
        if self.cleaned_data['options'] == 'member':
            group = Group.objects.get(name='Members')
            user.groups.add(group)
        else :
            group = Group.objects.get(name='Venues')
            user.groups.add(group)
        return user

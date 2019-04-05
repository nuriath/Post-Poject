from .models import Profile,Project,Rating
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user']



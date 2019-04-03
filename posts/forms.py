from .models import Profile,Project
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user','profile']

# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         exclude = ['user']

# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         exclude = ['user']

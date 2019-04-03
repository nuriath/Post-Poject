from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)
    project = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/')
    description = models.TextField(max_length =1000)
    link = models.CharField(max_length =600)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def get_project(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def search_by_username(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class Rating(models.Model):
    
    design  = models.CharField(max_length=30)
    usability = models.CharField(max_length=30)
    content = models.CharField(max_length =200)
    
    def __str__(self):
        return self.first_name

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()

    @classmethod
    def get_rating(cls):
        rating = cls.objects.all()
        return rating

    
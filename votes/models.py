from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

class Candidate():
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    position = models.CharField(max_length = 255)
    birthdate = models.DateTimeField(auto_now_add = True)
    platform = models.Textfield()
    
class Position():
    name = models.CharField(max_length = 255)
    desciption = models.CharField(max_length = 255)

class Vote():
    candidate = models.ForeignKey(Position, on_delete = models.CASCADE)
    vote_datetime = models.DateTimeField(auto_now_add = True)
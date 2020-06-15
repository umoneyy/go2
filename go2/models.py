"""
Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
"""

from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreation
from django.conf import settings
# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    steps = models.IntegerField(default=0)

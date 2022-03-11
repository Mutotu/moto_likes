from django.db import models
import uuid
from email.policy import default
# from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    username = models.CharField(max_length=200, blank=True, null=True)
    email=models.EmailField(max_length=500, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    
class Photo(models.Model):
    
    # user = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    user_id = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    photo=models.ImageField(null=True, blank=True, upload_to='likes/')
    
    created = models.DateTimeField(auto_now_add=True)
    
class Interaction(models.Model):
    
    LIKE_TYPE = (
        ('like', 'Like'),
        ('dislike', 'Dislike')
    )
    users = models.ManyToManyField(Profile)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # user_id = models.ForeignKey(Profile, null=True, blank=True, on_delete = models.SET_NULL)
    photo_id =  models.ForeignKey(Photo, null=True, blank=True, on_delete = models.SET_NULL)
    like = models.CharField(max_length=200, choices=LIKE_TYPE)
    comment = models.TextField(null=True, blank=True)
    like_total = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.like_total
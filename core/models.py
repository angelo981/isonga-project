from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class events(models.Model):
    title_en = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description_en = models.TextField()
    description_ar = models.TextField()
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title_en
class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('event', 'Event'),
        ('workshop', 'Workshop'),
        ('showcase', 'showcase'),
        ('performance', 'Performance'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="gallery/")
    video_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.subject}"
  
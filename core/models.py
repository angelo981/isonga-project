from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Event(models.Model):
    title_en = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', max_length=255) 
    description_en = models.TextField()
    category = models.ForeignKey(Category, null=False,  on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title_en
class Gallery(models.Model):
    GALLERY_CHOICES = [
        ('photo', 'Photo'),
        ('video', 'Video'),
    ]
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
    type = models.CharField(choices=GALLERY_CHOICES)
    image = models.ImageField(upload_to="gallery/", max_length=255)
    video_url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True, max_length=255) 
    sub_content = models.TextField(default="")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Talent(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='talents/', max_length=255)
    sub_content = models.TextField(default="")
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
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


class ProgramApplication(models.Model):
    PROGRAM_CHOICES = [
        ('youth_empowerment', 'Youth Empowerment & Skills Development'),
        ('digital_creative', 'Digital & Creative Skills'),
        ('media_broadcasting', 'Media & Broadcasting Basics'),
        ('talent_incubation', 'Talent Incubation'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    program_interest = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    why_join = models.TextField(help_text="Tell us why you want to join this program")
    experience = models.TextField(help_text="Any relevant experience or skills?", blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.get_program_interest_display()}"
  
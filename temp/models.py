from django.db import models

# Create your models here.
class Student(models.Model):
    COURSE_CHOICES = [
        ('cs', 'Computer Science'),
        ('bs', 'Business Studies'),
        ('hm', 'Hotel Management')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    
from django.db import models
from ckeditor.fields import RichTextField

class Question(models.Model):
    question = models.CharField(max_length=300, null=True, blank=True)
    answer = RichTextField(null=True, blank=True)
# Create your models here.

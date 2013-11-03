from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="tasks/")

class Hint(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    task = models.ForeignKey(Task)
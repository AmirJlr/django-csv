from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    matches = models.IntegerField()

    def __str__(self):
        return self.name

class CSV(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
    
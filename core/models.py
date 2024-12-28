from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    # description = models.TextField()
    img = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=225)
    second_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    message = models.TextField()


    def __str__(self):
        return self.email

class Plan(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.title
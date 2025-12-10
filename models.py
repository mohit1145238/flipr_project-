from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


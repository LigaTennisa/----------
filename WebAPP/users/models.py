from django.db import models

class RegisterForm(models.Model):
    name = models.EmailField(max_length=254)
    familia = models.CharField(max_length=30)
    mail = models.CharField(max_length=150)
    login = models.EmailField(max_length=254)
    parol = models.CharField(max_length=30)
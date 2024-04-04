from django.db import models

class Users(models.Model):
    name = models.CharField('имя', max_length=50)
    familia = models.CharField('фамилия', max_length=50)
    login = models.CharField('логин',max_length=50)
    parol = models.CharField('пароль',max_length=50)
    mail = models.CharField('почта', max_length=80) 
    
    def  __str__(self):
        return self.name
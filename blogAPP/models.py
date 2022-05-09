from pyexpat import model
from statistics import mode
from django.db import models

from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



# Create your models here.

class About(models.Model):
    about="Hola soy Joaquin Gomez y este es mi primer sitio web.Lo desarrolle utilizando Python con el framework Django,CSS y HTML5.Espero que te sea util!"


class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    numero=models.IntegerField()
    nacimiento=models.DateField()


    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.nombre}  {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    def __str__(self)->str:
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()


class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)
    









class Post(models.Model):
    CATEGORY_CHOICES = ( 
        ("1", "Programming/Technology"), 
        ("2", "Health/Fitness"), 
        ("3", "Personal"), 
        ("4", "Fashion"), 
        ("5", "Food"), 
        ("6", "Travel"), 
        ("7", "Business"), 
        ("8", "Art"),
        ("9", "Other"), 
    ) 


class Post1(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default='')
    snippet=models.CharField(max_length=255,default="Resumen")


    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('Article',args=(str(self.id)))

class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    webiste_url=models.CharField(max_length=255,default='')
    website_url=models.CharField(max_length=255,default='')

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('Inicio')
    

class Fotos(models.Model):
    fotos=models.ImageField(null=True,blank=True,upload_to="images/fotos/")

    


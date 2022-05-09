from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post1,Profile



class CursoForms(forms.Form):
    nombre= forms.CharField()
    camada= forms.CharField()


class EstudianteForms(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email=forms.EmailField()

class ProfesorForms(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()


class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='Usuario',widget=forms.TextInput)
    email=forms.EmailField()
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    last_name= forms.CharField(label='Apellido',widget=forms.TextInput)
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput)

class Meta:
    model=User
    fields=['username','email','password1','password2', 'last_name','first_name']
    help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar E-mail")
    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repetir la contraseña',widget=forms.PasswordInput)

    last_name= forms.CharField(label='Apellido',widget=forms.TextInput)
    first_name = forms.CharField(label='Nombre',widget=forms.TextInput)
    imagen = forms.ImageField()


    class Meta:
        model=User
        fields=['email','password1','password2','last_name','first_name']
        help_texts={k:"" for k in fields}


class PostForm(forms.ModelForm):
    class Meta:
        model=Post1
        fields=('title','title_tag','author','category','body','snippet','header_image')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),

            'title_tag': forms.TextInput(attrs={'class':'form-control'}),

            'author': forms.TextInput(attrs={'class':'form-control','value':'',id:'elder'}),

            #'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),

            'body': forms.Textarea(attrs={'class':'form-control'}),

            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }
        

class EditProfileForm(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
    
class ProfilePageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','website_url')
        widgets={
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'website_url':forms.TextInput(attrs={'class':'form-control'}),
            
            #'profile_pic':forms.
            }

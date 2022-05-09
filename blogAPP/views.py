from email import message
from multiprocessing import context
from pyexpat import model
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Avatar, Curso,Estudiante,Profesor,Familiar, Post1, Profile
from .forms import CursoForms,EstudianteForms,ProfesorForms, UserRegisterForm,UserEditForm,EditProfileForm,ProfilePageForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm ,UserChangeForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from Blog1.settings import EMAIL_HOST_USER
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

class AboutUs(LoginRequiredMixin,TemplateView):
    template_name="AppCoder/about.html"
    def get(self,request):
    
        return render(request,self.template_name)


@login_required
def formularioContacto(request):
    
   
    return render(request,"formularioContacto.html")

@login_required
def contactar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para =["sabinajoaquin38@gmail.com"]
        send_mail(asunto,mensaje,email_desde,email_para,fail_silently=False)
        return render(request,"contactoExitoso.html",{"url":avatares[0].imagen.url})
    return render(request,"formularioContacto.html",{"url":avatares[0].imagen.url})







def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user = authenticate(username=usuario,password=contra)

            if user is not None:
                login(request,user)


                return render(request,"AppCoder/index.html")

            else:

                return render(request,"AppCoder/index.html")

        else:

                return render(request,"AppCoder/index.html")
                
                
    form= AuthenticationForm()
    
    return render(request,"v3/login.html",{'form':form})



def register(request):
    if request.method == 'POST':

        form=UserRegisterForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/index.html",{"mensaje":"Usuario Creado"})

    
    else:
        form=UserRegisterForm()

    return render(request,"v3/register.html",{"form":form})

    



class CursoDetailView(LoginRequiredMixin,DetailView):
    model=Curso
    template_name='cbv/index_detailview.html'


class CursoList(LoginRequiredMixin,ListView):
    model=Curso
    template_name="cbv/index.html"

class CursoCreacion(LoginRequiredMixin,CreateView):
    model=Curso
    template_name='cbv/curso_form.html'
    success_url="/"
    fields=['nombre','camada']

class CursoUpdate(LoginRequiredMixin,UpdateView):
    model=Curso
    template_name= 'cbv/editarProfesor.html'
    success_url="/"
    fields=['nombre','camada']

class CursoDelete(LoginRequiredMixin,DeleteView):
    model=Curso
    template_name='cbv/curso_confirm_delete.html'
    success_url="/"


@login_required
def listado_familia(request):
   
    template = loader.get_template('listado_familia.html')
    familiares=Familiar.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))



@login_required
def inicio(request):
    return render(request, "AppCoder/index.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")
def cursoFormulario(request):
    return render(request, "AppCoder/cursoFormulario.html")


class ProfesorView(LoginRequiredMixin,TemplateView):
    template_name= "crud/profesor.html"
    def get(self, request):
        context={ 'profesores': Profesor.objects.all()
        }
        
        return render(request,self.template_name,context)

class ProfesorDeleteView(LoginRequiredMixin,TemplateView):
    template_name= "crud/profesor.html"
    def get(self, request, profesor_id):

        profesor=Profesor.objects.get(id=profesor_id)
        profesor.delete()
        #Profesor.objects.filter(id=profesor_id).delete()
        context={ 'profesores': Profesor.objects.all()
        }
        
        return render(request,self.template_name,context)

class ProfesorCreateUpdateView(LoginRequiredMixin,TemplateView):
    template_name= "crud/crear-profesor.html"
    def get(self, request,profesor_id=None):
        profesor=None

        if profesor_id:
            profesor = Profesor.objects.get(id=profesor_id)

        if profesor:

             context={'form3': ProfesorForms(
                 initial={
                     'nombre':profesor.nombre,
                     'apellido':profesor.apellido,
                     'email':profesor.email,
                     'profesion':profesor.profesion,

                 }
             )
        }
       
        else:
            context={'form3': ProfesorForms()
            }
        
        return render(request,self.template_name,context)

    def post(self,request,profesor_id=None):
        obj_post=request.POST

        Profesor.objects.update_or_create(
            email=obj_post.get('email'),
            defaults={
                'nombre':obj_post.get('nombre'),
                'apellido':obj_post.get('apellido'),
                'profesion':obj_post.get('profesion'),

            }
        )



  
        

        context={"form3":ProfesorForms()
        }
        return render(request,self.template_name,context)


class FormularioView(LoginRequiredMixin,TemplateView):
    template_name="forms/index.html"
    def get(self,request):
        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }
        return render(request,self.template_name,context)

    def post(self,request):

        response=CursoForms(request.POST)
        if response.is_valid:
            
            obj_response=response.cleaned_data

            nombre=obj_response["nombre"]
            camada=obj_response["camada"]
            print(f"CURSO:{nombre}")
            print(f"CAMADA:{camada}")
        
            obj_curso = Curso(nombre=obj_response.get("nombre"), camada=obj_response.get("camada"))
            obj_curso.save()

        response1=EstudianteForms(request.POST)
        if response1.is_valid:
            obj_response1=response1.cleaned_data
            obj_estudiante = Estudiante(nombre=obj_response1.get("nombre"), apellido=obj_response1.get("apellido"),email=obj_response1.get("email"))
            obj_estudiante.save()
       
        response2=ProfesorForms(request.POST)
        if response2.is_valid:
            obj_response2=response2.cleaned_data
            obj_profesor = Profesor(nombre=obj_response2.get("nombre"), apellido=obj_response2.get("apellido"),email=obj_response2.get("email"),profesion=obj_response2.get("profesion"))
            obj_profesor.save()

        context={
            "form":CursoForms(),
            "form1":EstudianteForms(),
            "form2":ProfesorForms(),
        }

        return render(request,self.template_name,context)

class SearchView(LoginRequiredMixin,TemplateView):
    template_name= "forms/search.html"

    def post(self,request):

        context={
            "elements":Curso.objects.filter(camada=request.POST.get("camada"))
        }

        return render(request,self.template_name,context)


"""@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=='POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data

            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request,"AppCoder/index.html")

    else:

        miFormulario= UserEditForm(initial={'email':usuario.email})


    return render(request,"v3/editarPerfil.html",{"miFormulario":miFormulario,"usuario":usuario})"""

class UserEditView(generic.UpdateView):
    form_class= EditProfileForm
    template_name='user/user_edit.html'
    success_url=reverse_lazy('Inicio')

    def get_object(self):
        return self.request.user

class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name= 'user/user_edit_page.html'
    fields=['bio','profile_pic']
    success_url= reverse_lazy('Inicio')      


@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST,request.FILES)

        if miFormulario.is_valid:
            u= User.objects.get(username=request.user)

            avatar=Avatar(user=u,imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request,"AppCoder/index.html")
    
    else:

        miFormulario=AvatarFormulario()

    return render(request,"AppCoder/agregarAvatar.html",{"miFormulario":miFormulario})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post1
    fields = ['title','title_tag','author','category','body','header_image']
    template_name = 'post/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostView(ListView):
    model=Post1
    template_name='post/blog_post.html'

class ArticleView(DetailView):
    model=Post1
    template_name="post/article.html"


class UpdatePostView(UpdateView):
    model=Post1
    template_name='post/update_post.html'
    fields=['title','title_tag','body','header_image']


class DeletePostView(DeleteView):
     model=Post1
     template_name='post/delete_post.html'
     success_url=reverse_lazy('Blog')


class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('Inicio')

class CreateProfilePageView(CreateView):
    model=Profile
    form_class=ProfilePageForm
    template_name="v3/create_user_profile_page.html"

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    





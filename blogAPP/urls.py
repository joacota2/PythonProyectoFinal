from django.urls import include, path
from .views import AboutUs, CursoCreacion, CursoDetailView, CursoUpdate, DeletePostView, ProfesorView,  SearchView, formularioContacto, listado_familia,contactar,UserEditView,PasswordsChangeView,CreateProfilePageView
from blogAPP import views
from django.views.generic import TemplateView
from .views import FormularioView, SearchView,ProfesorView, ProfesorCreateUpdateView, ProfesorDeleteView,CursoList,CursoDetailView, CursoCreacion,CursoUpdate,CursoDelete,PostView,ArticleView,UpdatePostView,EditProfilePageView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("familiares/",listado_familia),
    
    path("",views.inicio,name="Inicio"),
    path("cursos",views.cursos,name="Cursos"),
    path("cbv-curso",CursoList.as_view(),name="cbv-curso"),
    path("detail-curso/<int:pk>/",CursoDetailView.as_view(),name="detail-curso"),
    path("profesores",views.profesores),
    path("estudiantes",views.estudiantes),
    path("entregables",views.entregables),
    path("home/",views.inicio),
   # path("home/",TemplateView.as_view(template_name="AppCoder/home.html"),name="home"),
    path("formulario",FormularioView.as_view(),name="formulario"),
    path("search",SearchView.as_view(),name="search"),
    path("profesorview",ProfesorView.as_view(),name="profesorview"),
    path("profesor-delete-view/<int:profesor_id>",ProfesorDeleteView.as_view(),name="profesor-delete-view"),
    path("crear-profesor-view",ProfesorCreateUpdateView.as_view(),name="crear-profesor-view"),
    path("update-profesor-view/<int:profesor_id>",ProfesorCreateUpdateView.as_view(),name="profesor-update-view"),
    path("nuevo/",CursoCreacion.as_view(),name="new"),
    path("editar/<int:pk>/",CursoUpdate.as_view(),name="edit"),
    path("borrar/<int:pk>/",CursoDelete.as_view(),name="delete"),
    path('login/',views.login_request,),
    path('register/',views.register,),
    path('logout/',LogoutView.as_view(template_name='v3/logout.html'),name='logout'),
    path('formularioContacto/',formularioContacto),
    path('contactar/',contactar),
    path('about/',AboutUs.as_view(),name="about"),
    #path('editarPerfil/',views.editarPerfil,name="EditarPerfil"),
    path('editarPerfil/',UserEditView.as_view(),name="EditarPerfil"),
    path('<int:pk>/editarPerfil2/',EditProfilePageView.as_view(),name='editarPerfil2'),
    path('crearPerfil/',CreateProfilePageView.as_view(),name="CrearPerfil"),

    path('post/', views.PostCreateView.as_view(), name='add_post'),
    path('blog/',PostView.as_view(),name="Blog"),
    path('article/<int:pk>',ArticleView.as_view(),name="Article"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="Update"),
    path('article/<int:pk>/delete',DeletePostView.as_view(),name="Delete"),
    path('password/',auth_views.PasswordChangeView.as_view(template_name='user/change-password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='user/change-password.html')),




    ]

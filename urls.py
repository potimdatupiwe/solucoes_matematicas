from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.polinomio2, name='polinomio2'),
    path('Equacao_diofantina', views.equadio, name='equacaodio'),
    path('number', views.number, name='number'),
    path('teoch', views.teoch, name='teoch'),
    path('historic', views.historic, name='historic'),
    path('cadastro', views.cadastro,name='cadastro'),
    path('mudarsenha',views.mudarsenha,name='mudarsenha')

]
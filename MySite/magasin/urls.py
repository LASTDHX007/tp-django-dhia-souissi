from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('<int:myid>',views.detail, name="detail"),
    path('checkout/',views.checkout, name="checkout"),


    path('AjoutProduit/',views.index,name='ajout') ,
    path('register/',views.register, name = 'register'),
    # path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour') ,
    # path('commandes/',views.com,name='commandes') ,
    # path('admin/',views.com,name='admin') ,
    # path('admin/',views.com,name='admin') ,


]
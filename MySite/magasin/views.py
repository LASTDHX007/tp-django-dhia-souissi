from importlib import readers
from .models import Fournisseur, Produit,Commande
from .forms import ProduitForm 
from django.shortcuts import redirect ,render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required 
from .forms import ProduitForm,FournisseurForm ,UserRegistrationForm 
from django.contrib.auth import login, authenticate 
from django.contrib import messages 


def index(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide 
    return render(request,'magasin/majProduits.html',{'form':form})

def home(request):

    list=Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name !='' and item_name is not None:
        list = Produit.objects.filter(libellé__icontains=item_name)
    paginator = Paginator(list, 8)
    page = request.GET.get('page')
    list = paginator.get_page(page)
    return render(request,'magasin/home.html',{'list':list})

@login_required 
def homee(request): 
    context={'val':"Menu Acceuil"} 
    return render(request,'magasin/home.html',context) 


def register(request): 
    if request.method == 'POST' : 
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password)
            login(request,user)  
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')    
            return redirect('home') 
    else : 
        form = UserRegistrationForm() 
    return render(request,'registration/register.html',{'form' : form}) 



def detail(request, myid):
    list = Produit.objects.get(id=myid)
    return render(request,'magasin/detail.html', {'list': list}) 

def checkout(request):
    return render(request, 'magasin/checkout.html')

def nouveauFournisseur(request) :
    liste=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'liste':liste})


def com(request):
    commandes= Commande.objects.all()
    return render(request,'magasin/commande.html',{'commandes':commandes})
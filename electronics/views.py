from django.shortcuts import render
from electronics.models import Television, Speaker, Camera, AirConditioner
from garments.forms import ContactForm


def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    form = ContactForm
    return render(request, 'contactus.html', {'form':form})


def television(request):
    lst = Television.objects.all()
    return render(request, 'television.html', {'lst':lst})

def speaker(request):
    lst = Speaker.objects.all()
    return render(request, 'speaker.html', {'lst':lst})

def camera(request):
    lst = Camera.objects.all()
    return render(request, 'camera.html', {'lst':lst})

def airconditioner(request):
    lst = AirConditioner.objects.all()
    return render(request, 'airconditioner.html', {'lst':lst})


#Television Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Television, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})


#Camera Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Camera, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Speaker Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Speaker, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#AirConditioner Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(AirConditioner, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})
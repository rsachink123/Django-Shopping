from django.shortcuts import render, get_object_or_404
from garments.models import FormalShirt, FormalPant, Jean, TShirt
from garments.models import EthnicWear, Skirt, Beauty, Sandal, Handbag
from garments.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = 'Thank you for contacting us'
        message = 'This is your message:'+ request.POST.get('content')+'We will get back to you soon'
        from_email = settings.EMAIL_HOST_USER
        user_email = request.POST.get('contact_email')
        to_list = [user_email, settings.EMAIL_HOST_USER]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        return HttpResponseRedirect('thankyou')       
    return render(request, 'contactus.html', {'form':form})

def thankyou(request):
    response = HttpResponse()
    response.write("<h2>Thank you for contacting us.<br>We just sent you a mail.<br>So please check your mail.</h2>")
    return response

def formal_shirt(request):
    lst = FormalShirt.objects.all()
    return render(request, 'formal_shirt.html', {'lst':lst})

def formal_pant(request):
    lst = FormalPant.objects.all()
    return render(request, 'formal_pant.html', {'lst':lst})
def jean(request):
    lst = Jean.objects.all()
    return render(request, 'jean.html', {'lst':lst})
def tshirt(request):
    lst = TShirt.objects.all()
    return render(request, 'tshirt.html', {'lst':lst})
def ethnicwear(request):
    lst = EthnicWear.objects.all()
    return render(request, 'ethnicwear.html', {'lst':lst})
def skirt(request):
    lst = Skirt.objects.all()
    return render(request, 'skirt.html', {'lst':lst})
def beauty(request):
    lst = Beauty.objects.all()
    return render(request, 'beauty.html', {'lst':lst})
def sandal(request):
    lst = Sandal.objects.all()
    return render(request, 'sandal.html', {'lst':lst})
def handbag(request):
    lst = Handbag.objects.all()
    return render(request, 'handbag.html', {'lst':lst})

#FormalShirt Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(FormalShirt, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#FormalPant Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(FormalPant, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Jeans Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Jean, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#TShirt Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(TShirt, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#EthnicWear Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(EthnicWear, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Skirt Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Skirt, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Beauty Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Beauty, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Sandal Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Sandal, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})

#Handbag Cart
lst = []
price = []
def cart(request, id):
    item = get_object_or_404(Handbag, pk=id)
    lst.append(item)
    price.append(item.price)
    return render(request, 'cart.html', {'lst':lst, 'total_price':sum(price)})








  
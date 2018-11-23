"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from garments.views import index, aboutus,contactus,thankyou, formal_shirt, formal_pant,jean, tshirt, cart
from garments.views import ethnicwear, skirt, beauty, sandal, handbag
from electronics.views import television, speaker, camera, airconditioner

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^aboutus$', aboutus),
    url(r'^contactus$', contactus),
    url(r'^thankyou$', thankyou),
    url(r'^formal_shirt', formal_shirt),
    url(r'^formal_pant', formal_pant),
    url(r'^jean$', jean),
    url(r'^tshirt$', tshirt),
    url(r'^ethnicwear$',ethnicwear),
    url(r'^skirt$',skirt),
    url(r'^beauty$', beauty),
    url(r'^sandal$', sandal),
    url(r'^handbag$', handbag),
    url(r'^television$', television),
    url(r'^speaker$', speaker),
    url(r'^camera$', camera),
    url(r'^airconditioner$', airconditioner),
    url(r'^cart(\d{1,2})$', cart),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

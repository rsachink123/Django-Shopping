# Register your models here.
from django.contrib import admin
from garments.models import FormalShirt, FormalPant, Jean, TShirt
from garments.models import EthnicWear,Skirt,Beauty, Sandal, Handbag
class FormalShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(FormalShirt, FormalShirtAdmin)

class FormalPantAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(FormalPant, FormalPantAdmin)

class JeanAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Jean, JeanAdmin)

class TShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(TShirt, TShirtAdmin)

class EthnicWearAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(EthnicWear, EthnicWearAdmin)
class SkirtAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Skirt, SkirtAdmin)
class BeautyAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Beauty, BeautyAdmin)
class SandalAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Sandal, SandalAdmin)
class HandbagAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Handbag, HandbagAdmin)








# Register your models here.
from django.contrib import admin
from electronics.models import Television,Speaker,Camera,AirConditioner

class TelevisionAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Television, TelevisionAdmin)

class SpeakerAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Speaker, SpeakerAdmin)

class CameraAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(Camera, CameraAdmin)

class AirConditionerAdmin(admin.ModelAdmin):
    list_display=('name','price','desc','available', 'stock', 'created','updated')
admin.site.register(AirConditioner, AirConditionerAdmin)
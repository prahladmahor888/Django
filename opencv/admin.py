from django.contrib import admin
from opencv.models import createuser, UploadImage
class opencvAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'password')

class uploadImage(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(createuser, opencvAdmin)
admin.site.register(UploadImage, uploadImage)

# Register your models here.

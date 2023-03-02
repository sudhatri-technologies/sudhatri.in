from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','phoneNumber','message']
    

admin.site.register(Contact,ContactAdmin)

#username sudhatri
#password SriSudhatri@2022
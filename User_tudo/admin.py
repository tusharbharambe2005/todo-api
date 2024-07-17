from django.contrib import admin
from .views import User_model,tudo_list_model

# Register your models here.
class User_admin(admin.ModelAdmin):
    list_display=['user_id','user_name','user_email','user_number']
    search_fields=['user_name']
class tudo_admin(admin.ModelAdmin):
    list_display=['tudo_id','user_work','created']
    search_fields=['user_work']
    list_filter=['user_tudo_relation']

admin.site.register(User_model,User_admin)
admin.site.register(tudo_list_model,tudo_admin)



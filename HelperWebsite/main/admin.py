from django.contrib import admin
from .models import Contact,HelpRequest,Helper,Reply

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message')
   
admin.site.register(Contact,ContactAdmin)


class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'help_description', 'phone_number')
   
admin.site.register(HelpRequest,HelpRequestAdmin)


class HelperAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number','description_of_experiences', 'helper_cv')
   
admin.site.register(Helper,HelperAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('helprequest', 'user', 'content','created_at')
   
admin.site.register(Reply,ReplyAdmin)
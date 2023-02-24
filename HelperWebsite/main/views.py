from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact
# Create your views here.

#this function for home page
def home(request : HttpRequest):
   return render(request,'main/index.html') 

#this function for Contact form
def contact_form(request : HttpRequest):
   if request.method == "POST":
         add_contact =Contact(name= request.POST["name"], email = request.POST["email"], subject = request.POST["subject"], message = request.POST["message"])
         add_contact.save()
         return redirect("main:contact_received",contact_id=add_contact.id)
   
   return render(request,'main/contact.html')


#This function will work after the user submits the contact form 
def contact_received(request : HttpRequest,contact_id):
    contact_name=Contact.objects.get(id=contact_id)
    return render(request,'main/contact_received.html',{"contact_name":contact_name})


#this function for about us page
def about_us(request : HttpRequest):
   return render(request,'main/about.html') 


#this function for travel management helper page
def travel_management_helper(request : HttpRequest):
   return render(request,'main/travel_management_helper.html') 


#this function for event management helper page
def event_management_helper(request : HttpRequest):
   return render(request,'main/event_management_helper.html') 
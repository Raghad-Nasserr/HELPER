from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact,HelpRequest,Helper
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



######## user side 



#This function is for requests for help

def requests_for_help(request : HttpRequest):
    latest_help_requests = HelpRequest.objects.all()
    context = {"latest_help_requests" : latest_help_requests}
    return render(request,'main/requests_for_help.html',context)


#This function is for adding help request 

def add_help_request(request : HttpRequest):
   if request.method == "POST":
        #to add a new entry
        new_request = HelpRequest(user=request.user, help_description = request.POST["help_description"], phone_number = request.POST["phone_number"])
        new_request.save()
        return redirect("main:requests_for_help")

   return render(request,'main/add_help_request.html') 


#This function is for updating help request 

def update_help_request(request : HttpRequest,request_id):
   update = HelpRequest.objects.get(id=request_id)
   if request.method == "POST":
         update.phone_number = request.POST["phone_number"]
         update.help_description = request.POST["help_description"]
         update.save()
         return redirect("main:requests_for_help")
   return render(request,'main/update_help_request.html',{'update':update}) 


#This function is for deleting help request 

def delete_help_request(request : HttpRequest,request_id):
    delete_request = HelpRequest.objects.get(id=request_id)
    delete_request.delete()
    return redirect("main:requests_for_help")


#This function is for help details 

def help_details(request : HttpRequest,request_id):
    details=HelpRequest.objects.get(id=request_id)
    return render(request,'main/help_details.html',{'details':details}) 



## helper side


#this function for adding new helper
def add_new_helper(request : HttpRequest):
  if request.method == "POST":
         add_helper =Helper(name= request.POST["name"], email = request.POST["email"], phone_number = request.POST["phone_number"], description_of_experiences = request.POST["description_of_experiences"], helper_cv = request.FILES["helper_cv"])
         add_helper.save()
         return redirect("main:apply_page",apply_id=add_helper.id)
   
  return render(request,'main/add_new_helper.html')


#This function will work after the new helper submits the form 
def apply(request : HttpRequest,apply_id):
    helper=Helper.objects.get(id=apply_id)
    return render(request,'main/apply.html',{"helper":helper})
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Contact,HelpRequest,Helper,Reply
from django.contrib.auth.models import User
# Create your views here.

#This function for home page
def home(request : HttpRequest):
   return render(request,'main/index.html') 

#This function for Contact form
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


#This function for about us page
def about_us(request : HttpRequest):
   return render(request,'main/about.html') 


#This function for travel management helper page
def travel_management_helper(request : HttpRequest):
   return render(request,'main/travel_management_helper.html') 


#This function for event management helper page
def event_management_helper(request : HttpRequest):
   return render(request,'main/event_management_helper.html') 




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




#This function for adding new helper
def add_new_helper(request : HttpRequest):
  if request.method == "POST":
         new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"], first_name = request.POST["first_name"], last_name = request.POST["last_name"])
         new_user.save()
         add_helper =Helper(user= new_user, phone_number = request.POST["phone_number"], description_of_experiences = request.POST["description_of_experiences"], helper_cv = request.FILES["helper_cv"])
         add_helper.save()
         return redirect("accounts:login_user")
   
  return render(request,'main/add_new_helper.html')


#This function will work after the new helper submits the form 
def apply(request : HttpRequest,apply_id):
    helper=Helper.objects.get(id=apply_id)
    return render(request,'main/apply.html',{"helper":helper})




#This function to let the helper reply to help request 

def add_reply(request : HttpRequest,request_id):

    if request.method == "POST":
        helprequest = HelpRequest.objects.get(id=request_id)
        new_reply = Reply(user=request.user, helprequest=helprequest, content = request.POST["content"], created_at = request.POST["created_at"])
        new_reply.save()

    return redirect("main:help_details", request_id=request_id)



#This function is for help details 

def help_details(request : HttpRequest,request_id):
    helprequest=HelpRequest.objects.get(id=request_id)
    reply=Reply.objects.filter(helprequest=helprequest)
    return render(request,'main/help_details.html',{'helprequest':helprequest,'reply':reply}) 



#This function is for the helper profile 

def helper_profile(request : HttpRequest, user_id):
   user = User.objects.get(id=user_id)
   return render( request, "main/helper_profile.html", {"user" : user})



#This function is for the client profile 

def client_profile(request : HttpRequest):
   client=HelpRequest.objects.filter(user=request.user.id)
   return render( request, "main/client_profile.html",{'client':client})


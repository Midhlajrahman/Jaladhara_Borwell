import urllib.parse
from django.shortcuts import get_object_or_404, redirect, render 

from .forms import ContactForm, EnquiryForm
from .models import Services, Testimonial , Project


# Create your views here.
def index(request):
    context = {"testimonial": Testimonial.objects.all()}
    return render(request, "web/index.html", context)


def about(request):
    context = {"testimonial": Testimonial.objects.all()}
    return render(request, "web/about-us.html", context)


def services(request):
    context = {"service": Services.objects.all()}
    return render(request, "web/services.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = (
                f'Name: {form.cleaned_data["name"]} \n'
                f'Phone: {form.cleaned_data["phone"]}\n'
                f'Email: {form.cleaned_data["email"]}\n'
                f'Adress: {form.cleaned_data["adress"]} \n'
                f'Service: {form.cleaned_data["service"]} \n'
                f'Message: {form.cleaned_data["message"]}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943995533"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = (
                f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            )
            print('whatsapp_url==',whatsapp_url)
            return redirect(whatsapp_url)
        print(form.errors)
    
    context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact-us.html", context)


def service_details(request, slug):
    service = get_object_or_404(Services, slug=slug)
    form = EnquiryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.service =service
            data.save()
            print('==save====')
            message = (
                f'Enquery for: {data.service} \n\n'
                f'Name: {form.cleaned_data["full_name"]} \n'
                f'Phone: {form.cleaned_data["phone_number"]}\n'
                f'Adress: {form.cleaned_data["client_adress"]} \n'
                f'Message: {form.cleaned_data["description"]}\n'
            )

            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+918943995533"
            encoded_message = urllib.parse.quote(message)
            whatsapp_url = (
                f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            )
            return redirect(whatsapp_url)
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
        
    other_services = Services.objects.exclude(slug=slug)
    
    context["service"] = service
    context["other_services"] = other_services
    return render(request, "web/service_details.html", context)

def projects(request):
    context = {
     "projects":Project.objects.all() 
        
    }
    return render(request,'web/projects.html',context)

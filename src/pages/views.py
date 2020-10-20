from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# render(request, "template", {context})
# context is used in the template.html

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    my_context = {
        "my_text": "Contact me via 1234567890",
        "my_email": "karina.register@gmail.com",
        "my_list": [123,456,789]
    }
    return render(request, "contact.html", my_context)
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortenedURL
import random, string


# Create your views here.
#code is the shortened code(which is part of the shortened url)
#url is the long url

def index(request):
    #shows the form to enter the long url

    #shows a history of urls that the user has already shortened
    #uses ORM (object-relational mapper) to interact with the model field "code"
    url_history = ShortenedURL.objects.all()
    context = {
        "url_history": url_history,
    }

    return render(request, "tinyurl/index.html", context)

def code_generator():
    possibilities = string.ascii_letters + string.digits 
    code = ''
    length = 6
    x = 0
    while x < length:
        code += random.choice(possibilities)
        x += 1
    return code

def save_shortened(request):
    # print(request.POST)
    if 'longurl' not in request.POST:
        return HttpResponse('okay')
    #receives the form with the long url
    url = request.POST['longurl']

    # #generates a random string that will become the short url
    code = code_generator()

    model_instance = ShortenedURL(url = url, code = code)
    #saves the long and short urls to the database
    model_instance.save()
    return HttpResponseRedirect(reverse("tinyurl:index"))
    

# def redirection (request):
    #performs the redirecting to the target website
    #takes a short url as a parameter
    #include the protocol "https://" in the urls
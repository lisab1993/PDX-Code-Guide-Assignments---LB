from django.shortcuts import render

# Create your views here.
def index(request):
    greeting = 'meow'
    context = {
        'say_hello': greeting
    }
    return render(request, 'kittens_app/base.html', context)





    
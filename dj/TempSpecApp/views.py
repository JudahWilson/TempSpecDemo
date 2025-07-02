from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'name': 'John',
    }
    import os
    from pprint import pp
    pp(os.getcwd())
    pp(os.listdir('templates'))
    return render(request, 'home.html', context)

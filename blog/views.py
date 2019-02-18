from django.shortcuts import redirect

def redirect_home(request):
    show_home = redirect('home')
    return show_home

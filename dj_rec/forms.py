from django.shortcuts import render

def search_form(request):
    return render(request, 'templates/index.html')
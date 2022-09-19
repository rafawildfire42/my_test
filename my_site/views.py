from django.shortcuts import render

def clients(request):
    return render(request, "clients.html")

def clients_post(request):
    return render(request, "clients_post.html") 
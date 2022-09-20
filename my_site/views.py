from django.shortcuts import render

def clients(request):
    return render(request, "clients.html")

def clients_post(request):
    return render(request, "clients_post.html") 

def company(request):
    return render(request, "company.html")     

def company_post(request):
    return render(request, "company_post.html")     

def offert(request):
    return render(request, "offert.html")    
    
def offert_post(request):
    return render(request, "offert_post.html")     

def bid(request):
    return render(request, "bid.html")     

def bid_post(request):
    return render(request, "bid_post.html")     



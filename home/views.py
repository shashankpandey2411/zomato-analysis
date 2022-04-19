from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is About page")

def analysis(request):
    return HttpResponse("This is Analysis page")

def visualization(request):
    return HttpResponse("This is visualization page")
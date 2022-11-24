from django.shortcuts import render

# Create your views here.
def jinja_if (request):
    d={'a':123}
    return render(request,'jinja_if.html',d)

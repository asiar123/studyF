from django.shortcuts import render

# Create your views here.

def TermsAndConditions(request):
    return render(request, 'terms/terms.html')
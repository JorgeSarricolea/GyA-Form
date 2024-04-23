from django.shortcuts import render

# Create your views here.
def show_form(request):
  return render(request, 'form.html')
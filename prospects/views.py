from django.shortcuts import render, redirect
from .models import Prospect

def show_form(request):
    return render(request, 'form.html')

def create_prospect(request):
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mother_last_name = request.POST.get('mother_last_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            education_level = request.POST.get('education_level')
            currently_employed = request.POST.get('currently_employed') == 'True'
            sales_experience = request.POST.get('sales_experience') == 'True'

            # Create a new Prospect object with the form data
            prospect = Prospect(
                first_name=first_name,
                last_name=last_name,
                mother_last_name=mother_last_name,
                email=email,
                phone_number=phone_number,
                education_level=education_level,
                currently_employed=currently_employed,
                sales_experience=sales_experience
            )

            # Save the Prospect object to the database
            prospect.save()
            print('New lead successfully created!')
            return redirect('/prospects/')
        except Exception as e:
            print(f'Error creating prospect: {str(e)}')
            return redirect('/')
    else:
        return redirect('/')

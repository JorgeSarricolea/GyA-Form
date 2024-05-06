from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Prospect
import os

# List of email recipients
RECIPIENTS = [
    os.getenv('RECLUTA_EMAIL_A'),
    os.getenv('RECLUTA_EMAIL_B')
]
# Index to keep track of the last sent email
last_email_index = 0

# Shows popup form
def show_form(request):
    return render(request, 'form.html')

# Extracts form data from the request.
def get_form_data(request):
    if request.method == 'POST':
        return {
            'first_name': request.POST.get('first_name').capitalize(),
            'last_name': request.POST.get('last_name').capitalize(),
            'mother_last_name': request.POST.get('mother_last_name').capitalize(),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'education_level': request.POST.get('education_level'),
            'currently_employed': request.POST.get('currently_employed') == 'True',
            'sales_experience': request.POST.get('sales_experience') == 'True'
        }
    return None

# Saves the Prospect object to the database.
def save_prospect(data):
    prospect = Prospect(**data)
    prospect.save()
    print('New prospect successfully saved in DB!')
    return prospect

# Sends email to Recluta Team.
def send_email_to_recluta(prospect):
    try:
        global last_email_index
        to_email = RECIPIENTS[last_email_index]
        context = {'prospect': prospect}
        email_content = render_to_string('email/recluta.html', context)
        email = EmailMessage(
            subject='¡Nuevo prospecto registrado!',
            body=email_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email],
        )
        email.content_subtype = 'html'
        email.fail_silently = False
        email.send()
        print(f'Email sent to {to_email}!')
        last_email_index = (last_email_index + 1) % len(RECIPIENTS)
    except Exception as e:
        print(f'Error sending email to Recluta Team: {str(e)}')

# Sends thank you email to prospect.
def send_thank_you_email(prospect_email):
    try:
        context = {'prospect_email': prospect_email}
        email_content = render_to_string('email/thanks.html', context)
        email = EmailMessage(
            subject='¡Gracias por registrarte!',
            body=email_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[prospect_email],
        )
        email.content_subtype = 'html'
        email.fail_silently = False
        email.send()
        print(f'Thank you email sent to {prospect_email}!')
    except Exception as e:
        print(f'Error sending thank you email: {str(e)}')

# Creates a new prospect.
def create_prospect(request):
    try:
        form_data = get_form_data(request)
        if form_data:
            prospect = save_prospect(form_data)
            send_email_to_recluta(prospect)
            send_thank_you_email(prospect.email)
            return redirect('/prospects/')
    except Exception as e:
        print(f'Error creating prospect: {str(e)}')
    return redirect('/')

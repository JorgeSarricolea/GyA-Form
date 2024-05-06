from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Prospect
import os

# List of email RECLUTA_EMAILS
RECLUTA_EMAILS = os.getenv('RECLUTA_EMAILS').split(',')

# List of email recipients for Admin Team
ADMIN_EMAILS = os.getenv('ADMIN_EMAILS').split(',')

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

# Sends email to specified RECLUTA_EMAILS
def send_email(subject, body, to_emails):
    try:
        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.EMAIL_HOST_USER,
            to=to_emails,
        )
        email.content_subtype = 'html'
        email.fail_silently = False
        email.send()
        for to_email in to_emails:
            print(f'Email sent to {to_email}!')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

# Sends email to Recluta Team.
def send_email_to_recluta(prospect):
    global last_email_index
    to_email = RECLUTA_EMAILS[last_email_index]
    context = {'prospect': prospect}
    email_content = render_to_string('email/recluta.html', context)
    send_email('¡Nuevo prospecto registrado!', email_content, [to_email])
    last_email_index = (last_email_index + 1) % len(RECLUTA_EMAILS)

# Sends email to admin team
def send_email_to_admin(prospect):
    context = {'prospect': prospect}
    email_content = render_to_string('email/recluta.html', context)
    send_email('¡Nuevo prospecto registrado!', email_content, ADMIN_EMAILS)

# Sends thank you email to prospect.
def send_thank_you_email(prospect_email):
    context = {'prospect_email': prospect_email}
    email_content = render_to_string('email/thanks.html', context)
    send_email('¡Gracias por registrarte!', email_content, [prospect_email])

# Creates a new prospect.
def create_prospect(request):
    try:
        form_data = get_form_data(request)
        if form_data:
            prospect = save_prospect(form_data)
            send_email_to_recluta(prospect)
            send_thank_you_email(prospect.email)
            send_email_to_admin(prospect)
            return redirect('/prospects/')
    except Exception as e:
        print(f'Error creating prospect: {str(e)}')
    return redirect('/')

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

# Show popup form
def show_form(request):
    return render(request, 'form.html')

# Create a new prospect
def create_prospect(request):
    if request.method == 'POST':
        try:
            # Get form data
            first_name = request.POST.get('first_name').capitalize()
            last_name = request.POST.get('last_name').capitalize()
            mother_last_name = request.POST.get('mother_last_name').capitalize()
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
            print('New prospect successfully saved in DB!')

            # Send email to Recluta Team
            send_email_to_recluta(prospect)

            # Send email to prospect
            send_thank_you_email(prospect.email)

            return redirect('/prospects/')
        except Exception as e:
            print(f'Error creating prospect: {str(e)}')
            return redirect('/')
    else:
        return redirect('/')

# Send email to recluta team
def send_email_to_recluta(prospect):
    try:
        global last_email_index

        # Get the next email recipient
        to_email = RECIPIENTS[last_email_index]

        # Create context with prospect data
        context = {'prospect': prospect}

        # Render the email template with the context
        email_content = render_to_string('email/recluta.html', context)

        # Create and send the email message
        email = EmailMessage(
            subject='¡Nuevo prospecto registrado!',
            body=email_content,  # Pass the HTML content directly to the body
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email],
        )
        email.content_subtype = 'html'  # Set content type as HTML
        email.fail_silently = False

        # Send email to Recluta Team
        email.send()
        print(f'Email sent to {to_email}!')

        # Update the index for the next email
        last_email_index = (last_email_index + 1) % len(RECIPIENTS)
    except Exception as e:
        print(f'Error sending email to Recluta Team: {str(e)}')

# Send thank you email to prospect
def send_thank_you_email(prospect_email):
    try:
        # Create context for the email
        context = {'prospect_email': prospect_email}
        print(context)

        # Render the email template with the context
        email_content = render_to_string('email/thanks.html', context)

        # Create and send the email message
        email = EmailMessage(
            subject='¡Gracias por registrarte!',
            body=email_content,  # Pass the HTML content directly to the body
            from_email=settings.EMAIL_HOST_USER,
            to=[prospect_email],  # Send the email to the prospect's email address
        )
        email.content_subtype = 'html'  # Set content type as HTML
        email.fail_silently = False

        # Send the email
        email.send()
        print(f'Thank you email sent to {prospect_email}!')
    except Exception as e:
        print(f'Error sending thank you email: {str(e)}')

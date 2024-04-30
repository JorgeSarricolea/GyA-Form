from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Prospect

# Show popup form
def show_form(request):
    return render(request, 'form.html')

# Create a new prospect
def send_email_to_recluta(prospect):
    try:
        # Create context with prospect data
        context = {'prospect': prospect}

        # Render the email template with the context
        email_content = render_to_string('recluta_email_template.html', context)

        # Create and send the email message
        email = EmailMessage(
            subject='¡Nuevo prospecto registrado!',
            body=email_content,  # Pass the HTML content directly to the body
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
        )
        email.content_subtype = 'html'  # Set content type as HTML
        email.fail_silently = False

        # Send email to Recluta Team
        email.send()
        print('Email sent to Recluta Team!')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

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

            return redirect('/prospects/')
        except Exception as e:
            print(f'Error creating prospect: {str(e)}')
            return redirect('/')
    else:
        return redirect('/')
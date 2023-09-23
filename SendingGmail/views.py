# Import necessary modules and functions from Django's libraries
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib import messages
# Importing the ContactForm class from the local forms module
from .forms import ContactForm

# Defining a function-based view named 'sending_gmail' which handles the email sending logic
def sending_gmail(request):
    # Checking if the HTTP method of the request is POST (meaning the form was submitted)
    if request.method == "POST":
        # Initializing the ContactForm with the POST data
        form = ContactForm(request.POST)
        # Checking if the submitted form data is valid
        if form.is_valid():
            # Retrieving the cleaned data from the form
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
          
            # List of email recipients
            recipients = ['your_email@example.com']
            # Rendering the contact.html template to create an HTML email message
            html = render_to_string("contact.html", {
                "subject": subject,
                "message": message,
                "sender": sender
            })
            # Using Django's send_mail function to send the email
            send_mail(subject, message, sender, recipients, html_message=html)

            # Add a success message to be displayed on the webpage after redirection
            messages.info(request, 'Your message was sent successfully!')
            # Redirecting the user to the root/home page after successfully sending the email
            return redirect("/")

    # If the request method is not POST, initialize an empty ContactForm
    form = ContactForm()
    # Preparing the context dictionary to pass data to the template
    context = {
        "form": form
    }
    # Rendering the index.html template and passing the context data to it
    return render(request, "index.html", context)

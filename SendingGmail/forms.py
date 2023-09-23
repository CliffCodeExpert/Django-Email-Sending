# Importing necessary modules from Django's forms library.
from django import forms

# Defining a ContactForm class that inherits from forms.Form.
# This class will be used to represent and handle the form data.
class ContactForm(forms.Form):
    # Creating a CharField for the subject of the contact form.
    # This field will accept text up to 100 characters long.
    subject = forms.CharField(
        max_length=100,  # Maximum length is set to 100 characters.
        widget=forms.TextInput(  # Specifying the widget to be used for rendering this field in HTML.
            attrs={"placeholder": "Your Subject"}  # Setting placeholder attribute for the input field.
        ),
        label=" "  # Setting an empty label, likely to hide it and use placeholder instead.
    )

    # Creating a CharField for the message content in the contact form.
    # This field will accept text up to 200 characters long and will be rendered as a textarea.
    message = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={"placeholder": "Your Message"}  # Setting placeholder attribute for the textarea.
        ),
        label=" "
    )

    # Creating an EmailField to capture the sender's email address.
    # This field will ensure the input is a valid email format.
    sender = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "Your Email"}  # Setting placeholder attribute for the email input field.
        ),
        label=" "
    )

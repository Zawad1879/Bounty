from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):
    title = 'Enter Contact details'
    form = ContactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        print (form.cleaned_data)
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'First Django mail'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        title = 'Thanks!'
        confirm_message = 'Thanks for filling up the form. We will get right back to you'
        form = None

    context ={'title':title,'form':form, 'confirm_message':confirm_message}
    template = 'contact/contact.html'
    return render(request,template,context)

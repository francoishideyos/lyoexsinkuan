from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from .forms import SignUpForm
from django.contrib.auth import login, authenticate


# from .models import Party

# Create your views here.

def home(request):
    # parties = Party.objects.all()
    return render(request, 'home.html')

def rsvp(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # https://www.youtube.com/watch?v=51mmqf5a0Ss
            # if anything wrong with email reply (SMTP error)
            # https://accounts.google.com/DisplayUnlockCaptcha
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            subject = "Thank you!"
            message_text = "Dear " + str(post.name) + ", \nThank you for RSVP-ing, hope to see you on May 18th, 2019 at Angel's Share Cafe."
            message_html = "<p>Dear " + str(post.name) + ", \nThank you for RSVP-ing, hope to see you on May 18th, 2019 at <a href='https://goo.gl/maps/QrJoixZJDNu' target='_blank'>Angel's Share Cafe</a> <p>"
            from_email = settings.EMAIL_HOST_USER
            to_list = [post.email, settings.EMAIL_HOST_USER]
            
            msg = EmailMultiAlternatives(subject, message_text, from_email, to_list)
            msg.attach_alternative(message_html, "text/html")
            msg.send(fail_silently=False)

            # send_mail(subject, message_text, from_email, to_list,fail_silently=False)

            messages.success(request, 'Thank you for RSVP-ing, looking forward to see you!')
            
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'rsvp.html', {'form': form})
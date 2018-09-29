from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
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
            # send_mail(subject, message, from_email, to_list, fail_silently=True)
            subject = "Thank you!"
            message_text = "Dear " + str(post.name) + ", \nThank you for RSVP-ing, hope to see you soon!"
            
            from_email = settings.EMAIL_HOST_USER
            to_list = [post.email, settings.EMAIL_HOST_USER]
            
            send_mail(subject, message_text, from_email, to_list,fail_silently=False)
            messages.success(request, 'Thank you for RSVP-ing, looking forward to see you!')
            
            return redirect('../')
    else:
        form = SignUpForm()
    return render(request, 'rsvp.html', {'form': form})
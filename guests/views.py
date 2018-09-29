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
            message_text = "Dear " + str(post.name) + ", \n\nThank you for RSVP-ing, hope to see you on May 18th, 2019 at Angel's Share Cafe."
            #https://medium.com/django-musings/a-primer-on-sending-email-thru-django-40e3f6aa4355
            message_html = "<p>Dear " + str(post.name) + """,
				<br><br>

				Thank you for RSVP-ing, we are excited to see you on <b>May 18th, 2019 (Saturday)</b> late afternoon at <b><a href='https://goo.gl/maps/QrJoixZJDNu' target='_blank'>Angel's Share Cafe</a></b>.
				<br><br>

				As most of you are traveling from either Hong Kong or Singapore, here are some flights for your consideration:
				<br><br>

				From <a href='https://www.skyscanner.com.hk/transport/flights/hkga/tpet/190517/190519/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&currency=HKD#results' target='_blank'>Hong Kong</a>
				<br>
				From <a href='https://www.skyscanner.com.hk/transport/flights/sin/tpet/190517/190519/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=true&outboundaltsenabled=false&inboundaltsenabled=false&ref=home&currency=SGD#results' target='_blank'>Singapore</a>

				<br><br>
				For accodmodations, since the venue is near Shilin (士林), it will be convenient to stay near any major MRT stations. <br>
				<br>
				Some of our favorites which is right on top of Taipei station are:
				<br>
				<a href='https://www.trivago.hk/en?aDateRange%5Barr%5D=2019-05-17&aDateRange%5Bdep%5D=2019-05-19&aPriceRange%5Bto%5D=0&aPriceRange%5Bfrom%5D=0&iPathId=92369&aGeoCode%5Blat%5D=25.048704&aGeoCode%5Blng%5D=121.515045&iGeoDistanceItem=2227766&iGeoDistanceLimit=20000&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=222776602&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&' target='_blank'>iTaipei</a>
				<br>
				<a href='https://www.trivago.hk/en?aDateRange%5Barr%5D=2019-05-17&aDateRange%5Bdep%5D=2019-05-19&aPriceRange%5Bto%5D=0&aPriceRange%5Bfrom%5D=0&iPathId=556390&aGeoCode%5Blat%5D=25.049309&aGeoCode%5Blng%5D=121.517197&iGeoDistanceItem=4164892&iGeoDistanceLimit=20000&aCategoryRange=0%2C1%2C2%2C3%2C4%2C5&aOverallLiking=1%2C2%2C3%2C4%2C5&sOrderBy=relevance%20desc&bTopDealsOnly=false&iRoomType=7&cpt=416489202&iIncludeAll=0&iViewType=0&bIsSeoPage=false&bIsSitemap=false&' target='_blank'>Taipei Beautiful Apartment</a>
				<br><br>
				We are looking to arrange transportation to & from the venue when the date is closer, so please keep an eye out for updates.

				<br><br>
				Thank you very much & looking forward to see you!
				<br>
				#lyoexsinkuan

				<br><br>
				<small>p.s. <i> Updates will be communicated through <a href="https://chat.whatsapp.com/8yMkUG2PbAl1vJwT2Z89lK">Whatsapp group</a> & <a href='https://lyoexsinkuan.com' target='_blank'>lyoexsinkuan.com</a> </i></small>
				<p>
            """
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
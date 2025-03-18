from django.shortcuts import redirect, render
from .models import AuthForms
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from . tokens import generate_token 
from fifth import settings
import fit.views as fit_views



# Create your views here.
def Auth_view(request):
    auth_forms = AuthForms.objects.first()
    context = {
        'auth_forms':auth_forms,
    }
    return render(request, 'accounts/auth.html',context)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('index')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('index')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('index')
        
        if password != cpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('index')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('index')
            
        myuser = User.objects.create_user(username, email, password)
        myuser.fname = fname
        myuser.lname = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        # Welcome Email
        subject = "Welcome to fiftybit Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to fiftybit!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nShovit Nepal"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
            
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ FiftyBit - Django Login!!"
        message2 = render_to_string('mails/email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        send_mail(email_subject, message2, from_email, to_list, fail_silently=True)
        
        return redirect('index')
    return  redirect('index')


# that's for email confirmation link
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Your account has been activated successfully!")
        return redirect('index')
    else:
        messages.error(request, "Your account has been activated successfully!")
        return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user     = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You Have Successfully logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid username and password")
    return(request,"index")

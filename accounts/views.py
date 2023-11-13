from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .emails import send_verification_email, send_password_reset_email
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm


def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(user, request)
            return redirect("signup_success")
    else:
        form = SignupForm()
    return render(request=request, template_name="accounts/register.html", context={"form": form})


def login_user(request):
    if request.user.is_authenticated:
        # user is already logged in, take to the profile page
        return render(request, "accounts/profile.html", context={})

    login_failed = False
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("user_profile")
            else:
                login_failed = True
    else:
        form = LoginForm()
    return render(request=request, template_name="accounts/login.html", context={"form": form, 'failed': login_failed})


@login_required
def logout_view(request):
    logout(request)
    return redirect("login_user")


@login_required
def user_profile(request):
    return render(request, "accounts/profile.html", context={})


def verify_email_view(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        success = True
    else:
        success = False

    return render(request, "accounts/email_verification.html", {'success': success})


def forgot_password_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(username=email).first()
            send_password_reset_email(user, request)
            return redirect('password_reset_requested')
    else:
        form = PasswordResetForm()
    return render(request, "accounts/passwords/reset_form.html", {'form': form})


def set_password_view(request, uidb64, token):
    user = get_user_from_token(uidb64, token)
    token_valid = True
    form = None

    if user is None:
        token_valid = False
    elif request.method == "POST":
        form = SetPasswordForm(user, data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('password_reset_complete')
    else:
        form = SetPasswordForm(user)

    return render(
        request,
        "accounts/passwords/set_password.html",
        {'form': form, 'token_valid': token_valid}
    )


def get_user_from_token(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return None

    if user is not None and default_token_generator.check_token(user, token):
        return user

    return user

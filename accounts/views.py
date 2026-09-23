from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()


# Create your views here.

def list_accounts(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, "accounts/list.html", context)


# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile = request.POST.get('profile')

        try:
            existing_user = User.objects.get(username=username)
            return render(request, 'accounts/signup.html', {'error': 'Username already exists.'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=password, profil=profile)
            return redirect('list_accounts')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Wrong Username or password'})

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def edit_profile(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'user': user
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('newpassword')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            user = User.objects.get(pk=pk)

            user.last_name = last_name
            user.set_password(password)
            user.first_name = first_name

            user.save()

            login(request, user)
            return redirect('home')

        except User.DoesNotExist:

            return render(request, 'accounts/editprofile.html', {'error': 'An error occured'})

    return render(request, 'accounts/editprofile.html', context)

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import UserDetails
from .forms import UserForm
from .models import District, Branch
# Create your views here.


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=username, password=pw)
        if user is not None:
            auth.login(request, user)
            return render(request, 'new_page.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('credentials:login')
    return render(request, 'login.html')


def signup(request):
    print('signup')
    if request.method == 'POST':
        print('inside')
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('credentials:signup')
            else:
                user = User.objects.create_user(username=username,
                                            password=password)
            user.save()
            print('user created')
            return redirect('credentials:login')
        else:
            print('Password not matching')
            messages.info(request, 'Password not matching')
            return redirect('credentials:signup')
        return redirect('credentials:signup')
    return render(request, "signup.html")


def user_account(request):
    # task = Task.objects.get(id=id)
    f = UserForm(request.POST or None)
    if f.is_valid():
        f.save()
        messages.info(request, 'Application submitted successfully.')
        # return redirect('/')
    return render(request, 'user_account.html', {'form':f})


def load_branch(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('branch')
    print(branches)
    print(district_id)
    return render(request, 'branch_dropdown_list.html',
                  {'branches':branches})
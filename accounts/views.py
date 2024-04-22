from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('website:index')
                else:
                    return render(request, 'accounts/login.html', {'form': form})

        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        else:
            form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('website:index')
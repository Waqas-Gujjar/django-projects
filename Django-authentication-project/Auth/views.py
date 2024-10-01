from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Registration view
def register_viwe(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after registration
        else:
            return render(request, 'auth/registers.html', {'form': form})  # Return the form with errors
    else:
        initial_data = {"username": '', "password1": '', "password2": ''}
        form = UserCreationForm(initial=initial_data)
        return render(request, 'auth/registers.html', {'form': form})


# Login view
def login_view(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard on successful login
        else:
            return render(request, 'auth/login.html', {'form': form})  # Return the form with errors
    else:
        initial_data = {"username": '', "password1": '', "password2": ''}
        form = AuthenticationForm(initial=initial_data)
        return render(request, 'auth/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout


# Dashboard view
def deshboard_view(request):
    return render(request, 'dashboard.html')

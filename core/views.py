# users/views.py (or core/views.py)
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def settings_view(request):
    # Add your settings logic here
    return render(request, 'products/settings.html')  # Create this template

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your login page after logout

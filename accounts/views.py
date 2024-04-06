from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login(request):
    # Your login logic here
    return render(request, 'accounts/login.html')



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})




from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users_hub.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):   
  return render(request, 'users_hub/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            return redirect('/users/login')
    else:
        form = UserRegisterForm()
    return render(request, 'users_hub/register.html', {'form': form})
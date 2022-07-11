from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import UserCreationFormFix


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationFormFix()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'POST':
            form = UserCreationFormFix(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')
            contex = {
                'form': UserCreationFormFix(),
            }
            return render(request, self.template_name, contex)

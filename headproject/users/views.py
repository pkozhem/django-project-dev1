import os
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import UserCreationFormFix, UserUpdateForm, ProfileUpdateForm
from .models import Profile

User = get_user_model()


class Register(TemplateView):
    template_name = 'registration/register.html'

    def post(self, request):
        form = UserCreationFormFix(request.POST) or None
        if form.is_valid():
            form.save()
            print('user')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            print('test)
            return redirect('home')

        messages.error(request, f'Invalid credentials. Try again')
        contex = self.get_context_data(form=form)
        return self.render_to_response(contex)

    def get(self, request, *args, **kwargs):
        context = {
            'form': UserCreationFormFix()
        }
        return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/change_info.html'

    def post(self, request, slug):
        pic_path_current = str(Profile.objects.get(user=request.user).image)
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserUpdateForm(post_data, instance=request.user)
        profile_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            pic_path_new = str(Profile.objects.get(user=request.user).image)
            messages.success(request, f'Your account has been successfully updated')
            if pic_path_current != pic_path_new and pic_path_current != 'default.png':
                os.remove('users/media/' + pic_path_current)
            return redirect('profile', slug=slug)

        context = self.get_context_data(user_form=user_form,
                                        profile_form=profile_form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

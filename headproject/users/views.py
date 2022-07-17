from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from .forms import UserCreationFormFix, UserUpdateForm, ProfileUpdateForm

User = get_user_model()


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

            messages.error(request, f'Invalid credentials. Try again')
            print(form.errors)
            contex = {
                'form': UserCreationFormFix(),
            }
            return render(request, self.template_name, contex)


class ProfileUpdateView(TemplateView):
    user_form = UserUpdateForm
    profile_form = ProfileUpdateForm
    template_name = 'users/change_info.html'
    MESSAGE_TAGS = {}

    def post(self, request, slug):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserUpdateForm(post_data, instance=request.user)
        profile_form = ProfileUpdateForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been successfully updated')
            return redirect('profile', slug=slug)

        context = self.get_context_data(user_form=user_form,
                                        profile_form=profile_form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
    model = User

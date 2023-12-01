from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm
from .models import CustomUser, Profile
from django.contrib.auth.views import PasswordChangeView, LogoutView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })
        
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'

class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile_edit.html'
    fields = ['dob']

    def get_object(self, queryset=None):
        return self.request.user

        
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        response = super().form_valid(form)
        return self.logout_user(response)

    def logout_user(self, response):
        return LogoutView.as_view()(self.request)
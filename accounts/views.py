from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import PasswordChangeView, LogoutView, PasswordResetView

from .forms import CustomUserCreationForm, CustomProfileChangeForm
from .models import CustomUser, Profile

from .models import Profile
from django.contrib.auth import get_user_model


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, self.template_name, {'form' : form })
    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        return response

        
class ProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = CustomProfileChangeForm
    template_name = 'profile_edit.html'
    class Meta:
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'biography': 'Biography',
            'picture': 'Profile Picture',
        }
        crispy_field_class = 'bg-info'

    def get_success_url(self):
        return reverse_lazy('profile_view', args=[str(self.request.user.profile.id)])

        
        
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        response = super().form_valid(form)
        return self.logout_user(response)

    def logout_user(self, response):
        return LogoutView.as_view()(self.request)
    
        
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_Form.html'
    success_url = reverse_lazy('password_reset_done')

    
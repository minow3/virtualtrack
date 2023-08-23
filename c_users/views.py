from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from .forms import SignUpForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
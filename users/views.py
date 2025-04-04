from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from .models import Cliente
from .forms import ClienteRegistrationForm

class ClienteRegisterView(CreateView):
    model = Cliente
    form_class = ClienteRegistrationForm
    template_name = "users/register_cliente.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm

# Create your views here.

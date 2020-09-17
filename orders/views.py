import stripe
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
    extra_context = {
        'stripe_key': settings.STRIPE_TEST_PUBLISHABLE_KEY,
    }


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=9939,
            currency='usd',
            description='Purshase all books',
            source=request.POST['stripeToken'],
        )
        return render(request, 'orders/charge.html')

# Create your views here.

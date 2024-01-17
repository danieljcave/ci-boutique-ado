from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OZNxQL0tz14PUOZCJIsn6H0EHsJR2v9TVwBrSl4ffXXceW0nzj1iIZsLrr3Di9aNGhrWFPOKTjgQRfqdRd1KL59002jnn8xmz',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
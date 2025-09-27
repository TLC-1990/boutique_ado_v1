from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.conf import settings

from bag.contexts import bag_contents

# Create your views here.

def checkout(request):
    bag= request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form' : order_form, 
        'stripe_public_key': 'pk_test_51SBM0DRx0Cgi5lo6FwlDbCeqadUVxMGYI0TXS38dzDXbEaDIHUeRxHekWG49n6fvM1iJ037KjCb4RK0dgQI1D44l00sdIdvD6M',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
    
    
    
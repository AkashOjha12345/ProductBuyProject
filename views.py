from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import stripe
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY

# Fixed products
PRODUCTS = [
    {"id": 1, "name": "Product A", "price": 1000},  # price in cents
    {"id": 2, "name": "Product B", "price": 2000},
    {"id": 3, "name": "Product C", "price": 3000},
]

def index(request):
    orders = Order.objects.filter(paid=True).order_by("-created_at")
    return render(request, "store/index.html", {"products": PRODUCTS, "orders": orders})

def create_checkout_session(request):
    if request.method == "POST":
        quantities = [int(request.POST.get(f"quantity_{p['id']}", 0)) for p in PRODUCTS]
        
        line_items = []
        order = Order.objects.create(stripe_payment_intent="temp")
        
        for product, qty in zip(PRODUCTS, quantities):
            if qty > 0:
                OrderItem.objects.create(
                    order=order,
                    product_name=product["name"],
                    quantity=qty,
                    price=product["price"]/100
                )
                line_items.append({
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": product["name"]},
                        "unit_amount": product["price"],
                    },
                    "quantity": qty,
                })

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url=request.build_absolute_uri("/success/") + f"?order_id={order.id}",
            cancel_url=request.build_absolute_uri("/cancel/"),
        )

        order.stripe_payment_intent = session.payment_intent
        order.save()

        return redirect(session.url, code=303)

def success(request):
    order_id = request.GET.get("order_id")
    if order_id:
        order = Order.objects.get(id=order_id)
        order.paid = True
        order.save()
    return redirect("index")

def cancel(request):
    return render(request, "store/cancel.html")


def index(request):
	return render(request,"index.html")

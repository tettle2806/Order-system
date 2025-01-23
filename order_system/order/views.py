from django.shortcuts import render

# Create your views here.

# order_system/order/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderForm
from django.shortcuts import get_object_or_404

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})# order_system/order/views.py


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order/delete_order.html', {'order': order})# order_system/order/views.py
def search_orders(request):
    query = request.GET.get('q')
    orders = Order.objects.all()
    if query:
        orders = orders.filter(models.Q(table_number__icontains=query) | models.Q(status__icontains=query))
    return render(request, 'order/search_orders.html', {'orders': orders})# order_system/order/views.py
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})# order_system/order/views.py
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'order/update_order_status.html', {'form': form, 'order': order})# order_system/order/views.py
def revenue_report(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)
    return render(request, 'order/revenue_report.html', {'total_revenue': total_revenue})
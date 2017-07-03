from django.shortcuts import render, redirect

# Create your views here.
from deals.models import PurchaseOrder, SupplyOffer
from directconnect.settings import POST_ORDER_STATUS


def manage_purchase_order(request, purchase_order_id):
    purchase_order = PurchaseOrder.objects.get(id=purchase_order_id)
    supply_offers = purchase_order.supplyoffer_set.all()
    join_purchases = purchase_order.purchaseorderline_set.exclude(purchaser=purchase_order.initiator)
    if request.GET:
        for id in request.GET['id']:
            supply_offer = SupplyOffer.objects.get(id=id)
            supply_offer.is_noticed = True
            supply_offer.save()
    return render(request, "purchase_orders/manage.html", {
        'header': "{}采购单细节".format(purchase_order.product.name),
        'breadcrumb': [{"href": '/deals/purchase_orders/dashboard', "name": "我的发布"}],
        'purchase_order': purchase_order,
        'supply_offers': supply_offers,
        'join_purchases': join_purchases,
    })


def purchase_orders_dashboard(request):
    user = request.user

    if user.purchaser_set.all():
        purchaser = user.purchaser_set.all()[0]
        if request.GET:
            p_o = PurchaseOrder.objects.get(id=int(request.GET['order_id']))
            p_o.make_deal()
        return render(request, 'purchase_orders/dashboard.html', {
            'header': '我的订单',
            'purchase_orders_oc': purchaser.purchaseorder_set.filter(status=POST_ORDER_STATUS[0]),
            'purchase_orders_or': purchaser.purchaseorder_set.filter(status=POST_ORDER_STATUS[1]),
            'purchase_orders_cp': purchaser.purchaseorder_set.filter(status=POST_ORDER_STATUS[2]),
        })
    else:
        return redirect("/clients/purchasers/new")
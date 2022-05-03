from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from api.models import Product, Order
from api.serializers import OrderSerializer


@csrf_exempt
def product_canvas(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error: ' + str(e)})
    canvas_list = product.canvas.all()
    canvas_json = [f.to_json() for f in canvas_list]

    if request.method == 'GET':
        return JsonResponse(canvas_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'added'})


@csrf_exempt
def product_review(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error: ' + str(e)})
    review_list = product.review.all()
    review_json = [f.to_json() for f in review_list]

    if request.method == 'GET':
        return JsonResponse(review_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'added'})


# CRUD
class OrderListGet(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderListCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderListUpdate(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class OrderListDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)




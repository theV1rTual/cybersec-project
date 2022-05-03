from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Product, Canvas, Review, Order
from api.serializers import ProductSerializer, CanvasSerializer, ReviewSerializer, OrderSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        product = Product.objects.order_by_name(request)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message': 'deleted'}, status=204)



@api_view(['GET', 'POST'])
def canvas_list(request):
    if request.method == 'GET':
        canvas = Canvas.objects.all()
        serializer = CanvasSerializer(canvas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CanvasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def canvas_detail(request, canvas_id):
    try:
        canvas = Canvas.objects.get(id=canvas_id)
    except Canvas.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CanvasSerializer(canvas)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CanvasSerializer(instance=canvas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        canvas.delete()
        return Response({'message': 'deleted'}, status=204)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['DELETE'])
def delete_order(request):
    permission_classes = (IsAuthenticated,)
    if request.method == 'DELETE':
        orders = Order.objects.all()
        orders.delete()
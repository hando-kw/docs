from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.cart.models import Cart
from api.helpers.utils import swagger_response

from .serializers import CartSerializer, CartResponseSerializer

class CartViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    @swagger_response(response_schema={
        200: CartResponseSerializer,
        400: None,
        401: None,
        404: None
    })
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().prefetch_related('service')
        total = int(sum([(item.service.offer_price or item.service.price )* item.quantity for item in queryset]))
        serializer = CartResponseSerializer({'total': total, 'items': queryset}).data
        return Response(serializer)

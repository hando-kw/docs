from django.db.models import Prefetch
from rest_framework import generics

from app.services.models import MainCategory, Service
from app.cart.models import Cart

from api.helpers.utils import swagger_response

from .serializers import ServicesCategoriesSerializer

class ServicesCategoriesView(generics.ListAPIView):
    serializer_class = ServicesCategoriesSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return MainCategory.objects.prefetch_related('sub_categories', 'sub_categories__services', 'services')
        return MainCategory.objects.prefetch_related(
            'sub_categories',
            Prefetch('sub_categories__services', queryset=Service.objects.prefetch_related(
                Prefetch('cart', queryset=Cart.objects.filter(user=self.request.user), to_attr='user_cart')
            )),
            Prefetch('services', queryset=Service.objects.prefetch_related(
                Prefetch('cart', queryset=Cart.objects.filter(user=self.request.user), to_attr='user_cart')
            ))
        )

    @swagger_response(response_schema={
        200: ServicesCategoriesSerializer,
        400: None,
        401: None,
        404: None
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

from app.lookups.models import City
from api.helpers.utils import swagger_response
from .serializers import CitySerializer

class CityListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = CitySerializer
    
    queryset = City.objects.all().order_by('created_at')
    
    @swagger_response({
        200: CitySerializer,
        400 : None,
        404: None,
    })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
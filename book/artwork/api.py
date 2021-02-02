from .models import Artwork
from .serializers import GatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def artAPI(request):
    all_gat = Artwork.objects.all()
    data = GatSerializer(all_gat, many=True).data
    return Response({'data': data})
from .models import Author
from .serializers import GatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def autAPI(request):
    all_gat = Author.objects.all()
    data = GatSerializer(all_gat, many=True).data
    return Response({'data': data})
from rest_framework import viewsets
from Api.models import *
from Api.serializers import *


# Create your views here.
class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = SolicitacaoSerializer

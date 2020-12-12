from rest_framework import viewsets
from Api.models import Pessoa
from Api.serializers import SolicitacaoSerializer


# Create your views here.
class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = SolicitacaoSerializer

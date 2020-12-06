from rest_framework import serializers
from Api.models import *
from Api.utils import *

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):

    endereco = EnderecoSerializer(read_only= False)

    class Meta:

        model = Pessoa
        fields = '__all__'
        extra_kwargs = {
            'score': {'read_only': True},
            'credito': {'read_only': True}
        }
    
    def create(self, attrs):

        attrs['score'] = get_score()
        attrs['endereco'] = Endereco.objects.create(**attrs.pop('endereco'))
        attrs['credito'] = Credito(attrs['score'], attrs['renda']).calcular_limite()

        pessoa = Pessoa.objects.create(**attrs)

        Solicitacao.objects.create(pessoa=pessoa)

        return pessoa


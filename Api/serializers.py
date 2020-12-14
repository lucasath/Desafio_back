from rest_framework import serializers
from Api.models import Endereco, Pessoa, Solicitacao
from Api.utils import Credito, get_score, Cpf

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = '__all__'

class SolicitacoesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = '__all__'


class SolicitacaoSerializer(serializers.ModelSerializer):

    endereco = EnderecoSerializer(read_only = False)
    solicitacoes = SolicitacoesSerializer(read_only=True ,many = True)
    
    renda = serializers.FloatField(write_only= True)
    class Meta:

        model = Pessoa
        fields = '__all__'
        extra_kwargs = {
            'score': {'read_only': True},
            'credito': {'read_only': True},
            'cpf': {'validators': []},
        }

    def create(self, attrs):
        endereco_attrs = attrs.pop('endereco')
        query_set = Endereco.objects.filter(**endereco_attrs)

        if query_set:
            endereco = query_set.first()
        else:
            endereco = Endereco.objects.create(**endereco_attrs)
            
        attrs['endereco'] = endereco
        
        renda = attrs.pop('renda')
        score = get_score()
        credito = Credito(score, renda).calcular_limite()
        
        query_set = Pessoa.objects.filter(cpf=attrs['cpf'])
        pessoa = Pessoa(**attrs)
        
        if query_set:
            pessoa.id = query_set.get().id
        
        pessoa.save()
 

        Solicitacao.objects.create(pessoa=pessoa, renda=renda, score=score, credito=credito)

        return pessoa

    def validate_cpf(self, cpf):
        message = None

        if len(cpf) != 11:
            message = 'cpf precisa ter 11 digitidos'

        elif not cpf.isnumeric():
            message = 'cpf tem que ser numerico.'

        if message:
            raise serializers.ValidationError(message)

        if not Cpf(cpf).is_valid():
            raise serializers.ValidationError('cpf inválido')

        return cpf

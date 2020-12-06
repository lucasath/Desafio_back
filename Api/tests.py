from django.test import TestCase, Client
from Api.models import *
from Api.utils import *
from Api.serializers import *
import json

# Create your tests here.
class PessoaModelsTests(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(
		pais="Brasil",
		estado="PI",
		cidade="Teresina",
		cep="64000000",
		bairro="Centro",
		rua="Joaquim nelson",
		numero="2502")

        self.score = get_score()
        self.renda = 1050
        self.credito = Credito(self.score, self.renda).calcular_limite()

        self.pessoa = Pessoa.objects.create(nome="joao",
        renda= self.renda,endereco=self.endereco,score=self.score,credito=self.credito
        )

    def test_verificar_estado(self):
        query = Pessoa.objects.get(nome = self.pessoa.nome)

        self.assertEqual(query.nome, self.pessoa.nome)
        self.assertEqual(query.renda, self.renda)
        self.assertEqual(query.endereco.estado, self.endereco.estado)

    def test_verificar_score_e_credito(self):
        query = Pessoa.objects.get(nome = self.pessoa.nome)

        self.assertIsNotNone(query.credito)
        self.assertIsNotNone(query.score)


class EndPointTest(TestCase):
    
    def setUp(self):
        self.endereco = Endereco.objects.create(
		pais="Brasil",
		estado="PI",
		cidade="Teresina",
		cep="64000000",
		bairro="Centro",
		rua="Joaquim nelson",
		numero="2502")

        self.score = get_score()
        self.renda = 1050
        self.credito = Credito(self.score, self.renda).calcular_limite()

        self.pessoa = Pessoa.objects.create(nome="joao",
        renda= self.renda,endereco=self.endereco,score=self.score,credito=self.credito
        )

        self.data_json = {
            "nome":"pedro",
            "renda": 1050,
            "endereco":{
            "pais":"Brasil",
            "estado":"PI",
            "cidade":"Teresina",
            "cep":"64000000",
            "bairro":"Centro",
            "rua":"Joaquim nelson",
            "numero":"2502"
                }
            }

        self.client = Client()

        self.endpoint = "/api/solicitacoes/"

    def test_endpoint(self):

        response = self.client.get(self.endpoint)
        data = Pessoa.objects.all()
        serialize = SolicitacaoSerializer(data, many=True)

        self.assertEqual(response.data, serialize.data)
        self.assertEqual(response.status_code, 200)

    def test_endpoint_inserir(self):

        response = self.client.post(
            self.endpoint,
            data=json.dumps(self.data_json),
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)

    def test_endpoint_deletar(self):

        query = Pessoa.objects.get(nome=self.pessoa.nome)
        response = self.client.delete('{}{}/'.format(self.endpoint, query.id))
        self.assertEqual(response.status_code, 204)


        
    


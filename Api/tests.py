from django.test import TestCase, Client
from Api.models import Endereco,Pessoa, Solicitacao
from Api.utils import get_score, Credito, Cpf
from Api.serializers import SolicitacaoSerializer
import json


class RegradeNegocioTests(TestCase):
    def setUp(self):
        self.renda = 1000

    def test_verificar_reprovado(self):
        valor_esperado = 0
        score = 250
        credito = Credito(score, self.renda).calcular_limite()

        self.assertEqual(credito, valor_esperado)

    def test_verificar_mil(self):
        valor_esperado = 1000
        score = 350
        credito = Credito(score, self.renda).calcular_limite()

        self.assertEqual(credito, valor_esperado)


    def test_verificar_cinquenta_porcento_da_renda_ou_renda(self):
        valor_esperado = 1000
        score = 650
        credito = Credito(score, self.renda).calcular_limite()

        self.assertEqual(credito, valor_esperado)


    def test_verificar_duzentos_porcento_da_renda(self):
        valor_esperado = 2000
        score = 850
        credito = Credito(score, self.renda).calcular_limite()

        self.assertEqual(credito, valor_esperado)

    def test_verificar_sem_limites(self):
        valor_esperado = 1000000
        score = 980
        credito = Credito(score, self.renda).calcular_limite()

        self.assertEqual(credito, valor_esperado)


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

        self.pessoa = Pessoa.objects.create(nome="joao",cpf="46635420509",
        endereco=self.endereco
        )

        self.solicitacao = Solicitacao.objects.create(pessoa=self.pessoa,renda= self.renda, score=self.score, credito=self.credito)

    def test_verificar_estado(self):
        query = Pessoa.objects.get(nome = self.pessoa.nome)
        query_solicitacao = Solicitacao.objects.get(pessoa=query)

        self.assertEqual(query.nome, self.pessoa.nome)
        self.assertEqual(query_solicitacao.renda, self.renda)
        self.assertEqual(query.endereco.estado, self.endereco.estado)

    def test_verificar_score_e_credito(self):
        query = Pessoa.objects.get(nome = self.pessoa.nome)
        query_solicitacao = Solicitacao.objects.get(pessoa=query)

        self.assertIsNotNone(query_solicitacao.credito)
        self.assertIsNotNone(query_solicitacao.score)


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

        self.pessoa = Pessoa.objects.create(nome="joao",cpf="46635420509",endereco=self.endereco
        )

        self.solicitacao = Solicitacao.objects.create(pessoa=self.pessoa,renda= self.renda, score=self.score, credito=self.credito)

        self.data_json = {
            "nome":"pedro",
            "renda": 1050,
            "cpf": "46635420509",
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

class ValidatorTest(TestCase):


    def test_validate_cpf(self):

        cpf_valido = "46635420509"

        self.assertTrue(Cpf(cpf_valido).is_valid())

    def test_validate_cpf_invalido(self):

        cpf_invalido = "16648822332"

        self.assertFalse(Cpf(cpf_invalido).is_valid())

    def test_validate_cpf_valor_repetido(self):
        
        cpf_valor_repetido = "11111111111"

        self.assertFalse(Cpf(cpf_valor_repetido).is_valid())

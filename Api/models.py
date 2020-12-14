from django.db import models

# Create your models here.

class Endereco(models.Model):
    pais = models.CharField(max_length=250)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=250)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=250)
    rua = models.CharField(max_length=250)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=250, blank=True, null=True)

class Pessoa(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.ForeignKey('Endereco', models.CASCADE)


class Solicitacao(models.Model):
    pessoa = models.ForeignKey('Pessoa', models.CASCADE, related_name='solicitacoes')
    data = models.DateField(auto_now=True)
    renda = models.FloatField()
    score = models.IntegerField()
    credito = models.FloatField()
    class Meta:
        verbose_name_plural = 'Solicitações'
        



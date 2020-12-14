import random

class Credito:


    def __init__(self, score, renda):

        self.score = score
        self.renda = renda
        self.REGRA_LIMITE = {
            range(1, 300): self._reprovado,
            range(300, 600): self._mil,
            range(600, 800): self._valor_minimo_se_cinquenta_porcento,
            range(800, 951): self._duzentos_porcento,
            range(951, 1000): self._sem_limite
        }


    def calcular_limite(self):  

        for _range, callback in self.REGRA_LIMITE.items():
            if self.score in _range:
                return callback()
        return self._reprovado()


    def _reprovado(self):

        return 0


    def _mil(self):

        return 1000


    def _valor_minimo_se_cinquenta_porcento(self):

        if self.renda * 0.5 < 1000:
            return self.renda
        return self.renda * 0.5


    def _duzentos_porcento(self):

        return self.renda * 2


    def _sem_limite(self):

        return 1000000



def get_score():
    return random.randint(1, 999)

class Cpf:
    
    
    def __init__(self, value):

        self._pesos = {
            'primeiro': [10, 9, 8, 7, 6, 5, 4, 3, 2],
            'segundo': [11, 10, 9, 8, 7, 6, 5, 4, 3, 2],
        }
    
        self.value = value

    def is_valid(self):

        self.value = list(map(int, self.value))
        
        valor_repetido = self._valida_se_repetido()

        if valor_repetido:
            return False

        primeiro_digito = self._valida_primeiro()
        segundo_digito = self._valida_segundo()

        return primeiro_digito and segundo_digito

    def _calcula_digito(self, peso):

        soma = 0
        for index in range(len(peso)):
            soma += self.value[index] * peso[index]

        resto = soma % 11

        if resto < 2:
            return 0

        return 11 - resto

    def _valida_primeiro(self):

        valor_esperado = self._calcula_digito(self._pesos['primeiro'])

        return self.value[-2] == valor_esperado


    def _valida_segundo(self):

        valor_esperado = self._calcula_digito(self._pesos['segundo'])

        return self.value[-1] == valor_esperado

    def _valida_se_repetido(self):
        
        return len(set(self.value)) == 1

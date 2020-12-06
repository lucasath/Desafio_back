import random

def status_credito(score, renda):

    if score in range(1, 300):
        status = 0

    elif score in range(300, 600):
        status = 1000
    
    elif score in range(600, 800):
        if renda*0.5 < 1000:
            status = 1000
        else:
            status = renda*0.5

    elif score in range(800, 951):
        status = renda*2

    else:
        status = 1000000

    return status


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
        return reprovado()

    
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
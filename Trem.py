class Trem:
    def __init__(self):
        self.posicao = 0
        self.atual = None
        self.ultimo = None
        self.numRepetido = 0
        self.contagemMovimento = 0
        self.posicoes = []

    def salvarPosicao(self):
        self.posicoes.append(self.posicao)

    def irEsquerda(self):
        self.posicao -= 1

    def irDireita(self):
        self.posicao += 1

    def repetidoReset(self):
        self.numRepetido = 0
        
    def repetidoAdd(self):
        self.numRepetido += 1

    def movidoAdd(self):
        self.contagemMovimento += 1

    def isRepetido(self):
        if self.ultimo == self.atual:
            return True
        return False

    def maxMovido(self):
        if self.contagemMovimento >= 50:
            return True
        return False
                
    def maxRepetido(self):
        if self.numRepetido >= 20:
            return True
        return False
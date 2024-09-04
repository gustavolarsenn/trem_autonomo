import unittest
import Trem

class TestTrem(unittest.TestCase):
    def setUp(self):
        self.trem = Trem.Trem()
        
    def test_salvarPosicao(self):
        self.trem.salvarPosicao()
        self.assertEqual(self.trem.posicoes, [0])

    def test_irEsquerda(self):
        self.trem.irEsquerda()
        self.assertEqual(self.trem.posicao, -1)

    def test_irDireita(self):
        self.trem.irDireita()
        self.assertEqual(self.trem.posicao, 1)

    def test_repetidoReset(self):
        self.trem.repetidoReset()
        self.assertEqual(self.trem.numRepetido, 0)

    def test_repetidoAdd(self):
        self.trem.repetidoAdd()
        self.assertEqual(self.trem.numRepetido, 1)

    def test_movidoAdd(self):
        self.trem.movidoAdd()
        self.assertEqual(self.trem.contagemMovimento, 1)

    def test_isRepetido(self):
        self.trem.ultimo = "ESQUERDA"
        self.trem.atual = "ESQUERDA"
        self.assertTrue(self.trem.isRepetido())

        self.trem.ultimo = "ESQUERDA"
        self.trem.atual = "DIREITA"
        self.assertFalse(self.trem.isRepetido())

    def test_maxMovido(self):
        self.trem.contagemMovimento = 49
        self.assertFalse(self.trem.maxMovido())

        self.trem.contagemMovimento = 50
        self.assertTrue(self.trem.maxMovido())

    def test_maxRepetido(self):
        self.trem.numRepetido = 19
        self.assertFalse(self.trem.maxRepetido())

        self.trem.numRepetido = 20
        self.assertTrue(self.trem.maxRepetido())

if __name__ == '__main__':
    unittest.main()
import unittest
from funcionvocales import contar_vocales

class funcionvocales(unittest.TestCase):

    def test_nada(self):

        resultado = contar_vocales("zzz")

        self.assertEqual(resultado, {})
    
    def test_contar_a(self):

        resultado = contar_vocales('cas')

        self.assertEqual(resultado, {'a': 1})



    def test_contar_aa(self):

        resultado = contar_vocales('casa')

        self.assertEqual(resultado, {'a': 2})



    def test_contar_bese(self):

        resultado = contar_vocales('bese')

        self.assertEqual(resultado, {'e': 2})



    def test_contar_besa(self):

        resultado = contar_vocales('besa')

        self.assertEqual(resultado, {'a': 1, 'e': 1})



    def test_contar_casanova(self):

        resultado = contar_vocales('casanova')

        self.assertEqual(resultado, {'a': 3, 'o': 1})



    def test_contar_mUrciElago(self):

        resultado = contar_vocales('mUrciElago')

        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})

    
    def test_contar_RiverPlate(self):

        resultado = contar_vocales('RiverPlate')

        self.assertEqual(resultado, {'a': 1, 'e': 2, 'i': 1})    


    def test_contar_suponieras(self):

        resultado = contar_vocales('suponieras')

        self.assertEqual(resultado, {'a': 1, "e" : 1, "i" : 1,"o" : 1, "u" : 1 })
    
    def test_contar_EuforIA(self):

        resultado = contar_vocales('EuforIA')

        self.assertEqual(resultado, { "a": 1, "e" : 1, "i" : 1,"o" : 1, "u" : 1} )

unittest.main() 
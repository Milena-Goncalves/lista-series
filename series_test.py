import unittest
from dataclasses import is_dataclass
from series import Serie
from series import remove_stream

# Classe para testar a classe Series


class TestSerie(unittest.TestCase):

    # Testa se a classe Serie é uma dataclass
    def dataClass_Serie(self):
        self.assertTrue(is_dataclass(Serie))

    # Define um setUp para a classe Serie
    def setUp(self):
        self.serie = Serie("titulo_test", "test", 10)

    # Testa o construtor da classe
    def test_construtor_serie(self):
        self.assertEqual(self.serie.titulo, "titulo_test")
        self.assertEqual(self.serie.genero, "test")
        self.assertEqual(self.serie.nota, 10)

    # Testa a função stream preferido
    def test_stream_preferido(self):
        self.serie.stream_preferido("Test")
        self.assertEqual(self.serie.stream_preferido("Test"))

    # Teste de erro para valores de entrada inválidos
    def test_melhor_nota(self):
        self.assertRaises(ValueError, self.serie.MelhoresNotas, ("teste"))


# Classe para testar a classe Remove Stream
class remove_stream_test(unittest.TestCase):
    # Testa valores inseridos em remove stream
    def test_remove_stream(self):
        self.assertAlmostEqual(remove_stream(['Test'], []))
        self.assertAlmostEqual(remove_stream(['Test1', 'Test2'], ['Test3']))
        self.assertAlmostEqual(remove_stream([1]), [1])

    # Teste de erro para valores de entrada inválidos
    def test_error(self):
        self.assertRaises(ValueError, remove_stream, ('Test'))


if __name__ == '__series__':
    unittest.main()

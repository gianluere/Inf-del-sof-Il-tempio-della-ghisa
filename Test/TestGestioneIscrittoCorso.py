import unittest

from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi
from servizi.controller.ControlloreCorso import ControlloreCorso


class TestIscrittiCorso(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.controllore_cliente = ControllerListaClienti()
        self.corsi = ControlloreListaCorsi()
        self.controllore_corso = ControlloreCorso(self.corsi.get_corso_by_index(1))

    def test_add_iscritto(self):
        self.cliente = self.controllore_cliente.get_cliente_by_id(1000)
        self.controllore_corso.aggiungi_iscritto_corso(self.cliente)
        self.corsi.save_data()
        self.iscritti_corso = self.controllore_corso.get_lista_iscritti_corso()
        self.assertIsNotNone(self.iscritti_corso)
        self.assertIn(self.cliente, self.iscritti_corso)

    def test_remove_iscritto(self):
        self.cliente = self.controllore_cliente.get_cliente_by_id(1000)
        #self.controllore_corso.aggiungi_iscritto_corso(self.cliente)
        self.controllore_corso.elimina_iscritto_corso_by_id(1000)
        self.corsi.save_data()
        self.iscritti_corso = self.controllore_corso.get_lista_iscritti_corso()
        self.assertIsNotNone(self.iscritti_corso)
        self.assertNotIn(self.cliente, self.iscritti_corso)

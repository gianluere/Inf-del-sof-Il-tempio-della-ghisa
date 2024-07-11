import os
import pickle
from unittest import TestCase

from Utilizzatore.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti


class TestGestioneListaClienti(TestCase):
    def test_add_cliente(self):
        self.cliente = Cliente(1000, "prova", "prova", "CIAOCIAO123", "12/12/2024", "prova@gmail.com", "1231213123",
                               "22")
        self.clienti = ControllerListaClienti()
        self.clienti.aggiungi_cliente(self.cliente)
        self.clienti.save_data()

        lista = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                lista = pickle.load(f)
        self.assertIsNotNone(lista)
        self.assertIn(self.cliente, lista)

    def test_remove_cliente(self):
        self.controller_clienti = ControllerListaClienti()
        self.cliente = self.controller_clienti.get_cliente_by_id(1000)
        lista = []
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                lista = pickle.load(f)
        self.assertIsNotNone(lista)
        self.assertIn(self.cliente, lista)
        self.controller_clienti.rimuovi_cliente_by_id(1000)
        self.controller_clienti.save_data()
        #self.cliente = self.controller_clienti.get_cliente_by_id(1000)
        if os.path.isfile('listaclienti/data/lista_clienti_salvata.pickle'):
            with open('listaclienti/data/lista_clienti_salvata.pickle', 'rb') as f:
                lista = pickle.load(f)
        self.assertIsNotNone(lista)
        self.assertNotIn(self.cliente, lista)

import os
import pickle
from unittest import TestCase

from Utilizzatore.model.Nutrizionista import Nutrizionista
from listanutrizionisti.controller.ControlloreListaNutrizionisti import ControllerListaNutrizionisti


class TestGestioneListaNutrizionisti(TestCase):
    def test_add_nutrizionista(self):
        self.nutrizionista = Nutrizionista(1000, "prova", "prova", "CIAOCIAO123", "12/12/2024", "prova@gmail.com",
                                           "1231213123", "22", "Dietista")
        self.nutrizionisti = ControllerListaNutrizionisti()
        self.nutrizionisti.aggiungi_nutrizionista(self.nutrizionista)
        self.nutrizionisti.save_data()

        self.lista_nutrizionisti = []
        if os.path.isfile('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle'):
            with open('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle', 'rb') as f:
                self.lista_nutrizionisti = pickle.load(f)

        self.assertIsNotNone(self.lista_nutrizionisti)
        self.assertIn(self.nutrizionista, self.lista_nutrizionisti)

    def test_remove_nutrizionista(self):
        self.controller_nutrizionisti = ControllerListaNutrizionisti()
        self.nutrizionista = self.controller_nutrizionisti.get_nutrizionista_by_id(1000)

        lista_nutrizionisti = []
        if os.path.isfile('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle'):
            with open('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle', 'rb') as f:
                lista_nutrizionisti = pickle.load(f)

        self.assertIsNotNone(lista_nutrizionisti)
        self.assertIn(self.nutrizionista, lista_nutrizionisti)
        self.controller_nutrizionisti.rimuovi_nutrizionista_by_id(1000)
        self.controller_nutrizionisti.save_data()
        #self.controller_nutrizionisti.get_nutrizionista_by_id(1000)

        if os.path.isfile('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle'):
            with open('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle', 'rb') as f:
                lista_nutrizionisti = pickle.load(f)

        self.assertIsNotNone(lista_nutrizionisti)
        self.assertNotIn(self.nutrizionista, lista_nutrizionisti)

import os
import pickle
from unittest import TestCase

from Utilizzatore.model.Allenatore import Allenatore
from listaallenatori.controller.ControlloreListaAllenatori import ControllerListaAllenatori


class TestGestioneListaAllenatori(TestCase):
    def test_add_allenatore(self):
        self.allenatore = Allenatore(1000, "prova", "prova", "CIAOCIAO123", "12/12/2024", "prova@gmail.com",
                                     "1231213123", "22", "Personal Trainer")
        self.allenatori = ControllerListaAllenatori()
        self.allenatori.aggiungi_allenatore(self.allenatore)
        self.allenatori.save_data()

        lista_allenatori = []
        if os.path.isfile('listaallenatori/data/lista_allenatori_salvata.pickle'):
            with open('listaallenatori/data/lista_allenatori_salvata.pickle', 'rb') as f:
                lista_allenatori = pickle.load(f)

        self.assertIsNotNone(lista_allenatori)
        self.assertIn(self.allenatore, lista_allenatori)

    def test_remove_allenatore(self):
        self.controller_allenatori = ControllerListaAllenatori()
        self.allenatore = self.controller_allenatori.get_allenatore_by_id(1000)

        lista_allenatori = []
        if os.path.isfile('listaallenatori/data/lista_allenatori_salvata.pickle'):
            with open('listaallenatori/data/lista_allenatori_salvata.pickle', 'rb') as f:
                lista_allenatori = pickle.load(f)

        self.assertIsNotNone(lista_allenatori)
        self.assertIn(self.allenatore, lista_allenatori)
        self.controller_allenatori.rimuovi_allenatore_by_id(1000)
        self.controller_allenatori.save_data()
        #self.controller_allenatori.get_allenatore_by_id(1000)

        if os.path.isfile('listaallenatori/data/lista_allenatori_salvata.pickle'):
            with open('listaallenatori/data/lista_allenatori_salvata.pickle', 'rb') as f:
                lista_allenatori = pickle.load(f)

        self.assertIsNotNone(lista_allenatori)
        self.assertNotIn(self.allenatore, lista_allenatori)







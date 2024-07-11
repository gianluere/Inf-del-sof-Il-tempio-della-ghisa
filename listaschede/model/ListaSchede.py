import os
import pickle


class ListaSchede():
    def __init__(self):
        self.lista_schede = []
        if os.path.isfile('listaschede/data/lista_schede_salvata.pickle'):
            with open('listaschede/data/lista_schede_salvata.pickle', 'rb') as f:
                self.lista_schede = pickle.load(f)

    def aggiungi_scheda(self, scheda):
        self.lista_schede.append(scheda)

    def rimuovi_scheda_by_id(self, id):
        def is_selected(scheda):
            if scheda.id == id:
                return True
            return False

        self.lista_schede.remove(list(filter(is_selected, self.lista_schede))[0])

    def get_scheda_by_id(self, id):
        for scheda in self.lista_schede:
            if scheda.id == id:
                return scheda

    def get_scheda_by_index(self, index):
        return self.lista_schede[index]

    def get_lista_schede(self):
        return self.lista_schede

    def save_data(self):
        with open('listaschede/data/lista_schede_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_schede, handle, pickle.HIGHEST_PROTOCOL)
import os
import pickle


class ListaNutrizionisti():
    def __init__(self):
        self.lista_nutrizionisti = []
        if os.path.isfile('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle'):
            with open('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle', 'rb') as f:
                self.lista_nutrizionisti = pickle.load(f)

    def aggiungi_nutrizionista(self, nutrizionista):
        self.lista_nutrizionisti.append(nutrizionista)

    def rimuovi_nutrizionista_by_id(self, id):
        def is_selected(nutrizionista):
            if nutrizionista.id == id:
                return True
            return False

        self.lista_nutrizionisti.remove(list(filter(is_selected, self.lista_nutrizionisti))[0])

    def get_nutrizionista_by_index(self, index):
        return self.lista_nutrizionisti[index]

    def get_nutrizionista_by_id(self, id):
        for nutr in self.lista_nutrizionisti:
            if nutr.id == id:
                return nutr

    def get_lista_nutrizionisti(self):
        return self.lista_nutrizionisti

    def save_data(self):
        with open('listanutrizionisti/data/lista_nutrizionisti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_nutrizionisti, handle, pickle.HIGHEST_PROTOCOL)
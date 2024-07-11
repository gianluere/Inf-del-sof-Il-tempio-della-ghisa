import os
import pickle

class ListaDiete():
    def __init__(self):
        self.lista_diete = []
        if os.path.isfile('listadiete/data/lista_diete_salvata.pickle'):
            with open('listadiete/data/lista_diete_salvata.pickle', 'rb') as f:
                self.lista_diete = pickle.load(f)

    def aggiungi_dieta(self, dieta):
        self.lista_diete.append(dieta)

    def rimuovi_dieta_by_id(self, id):
        def is_selected(dieta):
            if dieta.id == id:
                return True
            return False

        self.lista_diete.remove(list(filter(is_selected, self.lista_diete))[0])

    def get_dieta_by_id(self, id):
        for dieta in self.lista_diete:
            if dieta.id == id:
                return dieta

    def get_dieta_by_index(self, index):
        return self.lista_diete[index]

    def get_lista_diete(self):
        return self.lista_diete

    def save_data(self):
        with open('listadiete/data/lista_diete_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_diete, handle, pickle.HIGHEST_PROTOCOL)
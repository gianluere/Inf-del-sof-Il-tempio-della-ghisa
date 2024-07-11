import os
import pickle


class ListaAbbonamenti():
    def __init__(self):
        self.lista_abbonamenti = []
        if os.path.isfile('listaabbonamenti/data/lista_abbonamenti_salvata.pickle'):
            with open('listaabbonamenti/data/lista_abbonamenti_salvata.pickle', 'rb') as f:
                self.lista_abbonamenti = pickle.load(f)

    def aggiungi_abbonamento(self, abbonamento):
        self.lista_abbonamenti.append(abbonamento)

    def rimuovi_abbonamento_by_id(self, id):
        def is_selected(abbonamento):
            if abbonamento.id == id:
                return True
            return False

        self.lista_abbonamenti.remove(list(filter(is_selected, self.lista_abbonamenti))[0])

    def get_abbonamento_by_id(self, id):
        for abb in self.lista_abbonamenti:
            if abb.id == id:
                return abb

    def get_abbonamento_by_index(self, index):
        return self.lista_abbonamenti[index]

    def get_lista_abbonamenti(self):
        return self.lista_abbonamenti

    def save_data(self):
        with open('listaabbonamenti/data/lista_abbonamenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_abbonamenti, handle, pickle.HIGHEST_PROTOCOL)
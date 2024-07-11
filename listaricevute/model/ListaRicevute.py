import os
import pickle


class ListaRicevute():
    def __init__(self):
        self.lista_ricevute = []
        if os.path.isfile('listaricevute/data/lista_ricevute_salvata.pickle'):
            with open('listaricevute/data/lista_ricevute_salvata.pickle', 'rb') as f:
                self.lista_ricevute = pickle.load(f)

    def aggiungi_ricevuta(self, ricevuta):
        self.lista_ricevute.append(ricevuta)

    def get_ricevuta_by_id(self, id):
        for ric in self.lista_ricevute:
            if ric.id == id:
                return ric

    def rimuovi_ricevuta_by_id(self, id):
        def is_selected(ricevuta):
            if ricevuta.id == id:
                return True
            return False

        self.lista_ricevute.remove(list(filter(is_selected, self.lista_ricevute))[0])

    def get_ricevuta_by_index(self, index):
        return self.lista_ricevute[index]

    def get_lista_ricevute(self):
        return self.lista_ricevute

    def save_data(self):
        with open('listaricevute/data/lista_ricevute_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ricevute, handle, pickle.HIGHEST_PROTOCOL)
import os
import pickle


class ListaVisite():
    def __init__(self):
        self.lista_visite = []
        if os.path.isfile('listavisite/data/lista_visite_salvata.pickle'):
            with open('listavisite/data/lista_visite_salvata.pickle', 'rb') as f:
                self.lista_visite = pickle.load(f)

    def aggiungi_visita(self, visita):
        self.lista_visite.append(visita)

    def rimuovi_visita_by_id(self, id):
        def is_selected(visita):
            if visita.id == id:
                return True
            return False

        self.lista_visite.remove(list(filter(is_selected, self.lista_visite))[0])

    def get_visita_by_id(self, id):
        for visita in self.lista_visite:
            if visita.id == id:
                return visita

    def get_visita_by_index(self, index):
        return self.lista_visite[index]

    def get_lista_visite(self):
        return self.lista_visite

    def get_visita_by_codice_fiscale(self, codice_fiscale):
        for visita in self.lista_visite:
            if visita.codiceFiscale == codice_fiscale:
                return visita

    def save_data(self):
        with open('listavisite/data/lista_visite_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_visite, handle, pickle.HIGHEST_PROTOCOL)
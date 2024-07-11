import os
import pickle
from listaclienti.model.ListaClienti import ListaClienti
from listaallenatori.model.ListaAllenatori import ListaAllenatori
from listanutrizionisti.model.ListaNutrizionisti import ListaNutrizionisti

class ListaUtenti():
    def __init__(self):
        self.lista_utenti = []
        if os.path.isfile('listautenti/data/lista_utenti_salvata.pickle'):
            with open('listautenti/data/lista_utenti_salvata.pickle', 'rb') as f:
                self.lista_utenti = pickle.load(f)



    def aggiungi_utente(self, utente):
        self.lista_utenti.append(utente)

    def rimuovi_utente_by_id(self, id):
        def is_selected(utente):
            if utente.id == id:
                return True
            return False
        self.lista_utenti.remove(list(filter(is_selected, self.lista_utenti))[0])

    def get_utente_by_index(self, index):
        return self.lista_utenti[index]

    def get_utente_by_id(self, id):
        for utente in self.lista_utenti:
            if utente.id == id:
                return utente

    def get_lista_utenti(self):
        return self.lista_utenti

    def save_data(self):
        with open('listautenti/data/lista_utenti_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_utenti, handle, pickle.HIGHEST_PROTOCOL)
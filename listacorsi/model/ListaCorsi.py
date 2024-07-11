import os
import pickle


class ListaCorsi():
    def __init__(self):
        self.lista_corsi = []
        if os.path.isfile('listacorsi/data/lista_corsi_salvata.pickle'):
            with open('listacorsi/data/lista_corsi_salvata.pickle', 'rb') as f:
                self.lista_corsi = pickle.load(f)

    def aggiungi_corso(self, corso):
        self.lista_corsi.append(corso)

    def rimuovi_corso_by_id(self, id):
        def is_selected(corso):
            if corso.id == id:
                return True
            return False

        self.lista_corsi.remove(list(filter(is_selected, self.lista_corsi))[0])

    def get_corso_by_id(self, id):
        for corso in self.lista_corsi:
            if corso.id == id:
                return corso

    def get_corso_by_index(self, index):
        return self.lista_corsi[index]

    def get_lista_corsi(self):
        return self.lista_corsi

    def save_data(self):
        with open('listacorsi/data/lista_corsi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_corsi, handle, pickle.HIGHEST_PROTOCOL)
import os
import pickle


class ListaAllenatori():
    def __init__(self):
        self.lista_allenatori = []
        if os.path.isfile('listaallenatori/data/lista_allenatori_salvata.pickle'):
            with open('listaallenatori/data/lista_allenatori_salvata.pickle', 'rb') as f:
                self.lista_allenatori = pickle.load(f)
    
    def aggiungi_allenatore(self, allenatore):
        self.lista_allenatori.append(allenatore)

    def rimuovi_allenatore_by_id(self, id):
        def is_selected(allenatore):
            if allenatore.id == id:
                return True
            return False
        self.lista_allenatori.remove(list(filter(is_selected, self.lista_allenatori))[0])

    def get_allenatore_by_index(self, index):
        return self.lista_allenatori[index]

    def get_allenatore_by_id(self, id):
        for allen in self.lista_allenatori:
            if allen.id == id:
                return allen

    def get_lista_allenatori(self):
        return self.lista_allenatori

    def save_data(self):
        with open('listaallenatori/data/lista_allenatori_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_allenatori, handle, pickle.HIGHEST_PROTOCOL)
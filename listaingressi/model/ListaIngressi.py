import os
import pickle


class ListaIngressi():
    def __init__(self):
        self.lista_ingressi = []
        if os.path.isfile('listaingressi/data/lista_ingressi_salvata.pickle'):
            with open('listaingressi/data/lista_ingressi_salvata.pickle', 'rb') as f:
                self.lista_ingressi = pickle.load(f)

    def aggiungi_ingresso(self, ingresso):
        self.lista_ingressi.append(ingresso)

    def rimuovi_ingresso_by_id(self, id):
        def is_selected(ingresso):
            if ingresso.id == id:
                return True
            return False

        self.ingresso_.remove(list(filter(is_selected, self.lista_ingressi))[0])

    def get_ingresso_by_id(self, id):

        for ingresso in self.lista_ingressi:
            if ingresso.id == id:
                return ingresso

    def get_ingresso_by_index(self, index):
        return self.lista_ingressi[index]

    def get_lista_ingressi(self):
        return self.lista_ingressi

    def save_data(self):
        with open('listaingressi/data/lista_ingressi_salvata.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingressi, handle, pickle.HIGHEST_PROTOCOL)

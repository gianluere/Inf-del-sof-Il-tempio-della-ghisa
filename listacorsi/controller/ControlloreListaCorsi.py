from listacorsi.model.ListaCorsi import ListaCorsi


class ControlloreListaCorsi():
    def __init__(self):
        self.model = ListaCorsi()

    def aggiungi_corso(self, corso):
        self.model.aggiungi_corso(corso)

    def rimuovi_corso_by_id(self, id):
        self.model.rimuovi_corso_by_id(id)

    def get_corso_by_id(self, id):
        return self.model.get_corso_by_id(id)

    def get_corso_by_index(self, index):
        return self.model.get_corso_by_index(index)

    def get_lista_corsi(self):
        return self.model.get_lista_corsi()

    def save_data(self):
        self.model.save_data()
from listaricevute.model.ListaRicevute import ListaRicevute


class ControlloreListaRicevute():
    def __init__(self):
        self.model = ListaRicevute()

    def aggiungi_ricevuta(self, ricevuta):
        self.model.aggiungi_ricevuta(ricevuta)

    def get_ricevuta_by_id(self, id):
        return self.model.get_ricevuta_by_id(id)

    def rimuovi_ricevuta_by_id(self, id):
        self.model.rimuovi_ricevuta_by_id(id)

    def get_ricevuta_by_index(self, index):
        return self.model.get_ricevuta_by_index(index)

    def get_lista_ricevute(self):
        return self.model.get_lista_ricevute()

    def save_data(self):
        self.model.save_data()
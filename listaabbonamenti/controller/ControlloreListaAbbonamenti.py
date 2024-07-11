from listaabbonamenti.model.ListaAbbonamenti import ListaAbbonamenti


class ControlloreListaAbbonamenti():
    def __init__(self):
        self.model = ListaAbbonamenti()

    def aggiungi_abbonamento(self, abbonamento):
        self.model.aggiungi_abbonamento(abbonamento)

    def rimuovi_abbonamento_by_id(self, id):
        self.model.rimuovi_abbonamento_by_id(id)

    def get_abbonamento_by_id(self, id):
        return self.model.get_abbonamento_by_id(id)

    def get_abbonamento_by_index(self, index):
        return self.model.get_abbonamento_by_index(index)

    def get_lista_abbonamenti(self):
        return self.model.get_lista_abbonamenti()

    def save_data(self):
        self.model.save_data()

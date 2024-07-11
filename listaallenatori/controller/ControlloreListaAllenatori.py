from listaallenatori.model.ListaAllenatori import ListaAllenatori


class ControllerListaAllenatori():

    def __init__(self):
        self.model = ListaAllenatori()

    def aggiungi_allenatore(self, allenatore):
        self.model.aggiungi_allenatore(allenatore)

    def get_lista_allenatori(self):
        return self.model.get_lista_allenatori()

    def get_allenatore_by_index(self, index):
        return self.model.get_allenatore_by_index(index)

    def get_allenatore_by_id(self, id):
        return self.model.get_allenatore_by_id(id)

    def rimuovi_allenatore_by_id(self, id):
        self.model.rimuovi_allenatore_by_id(id)

    def save_data(self):
        self.model.save_data()
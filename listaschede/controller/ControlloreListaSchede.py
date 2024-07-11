from listaschede.model.ListaSchede import ListaSchede


class ControlloreListaSchede():
    def __init__(self):
        self.model = ListaSchede()

    def aggiungi_scheda(self, scheda):
        self.model.aggiungi_scheda(scheda)

    def rimuovi_scheda_by_id(self, id):
        self.model.rimuovi_scheda_by_id(id)

    def get_scheda_by_id(self, id):
        return self.model.get_scheda_by_id(id)

    def get_scheda_by_index(self, index):
        return self.model.get_scheda_by_index(index)

    def get_lista_schede(self):
        return self.model.get_lista_schede()

    def save_data(self):
        self.model.save_data()
from listavisite.model.ListaVisite import ListaVisite


class ControlloreListaVisite():
    def __init__(self):
        self.model = ListaVisite()

    def aggiungi_visita(self, visita):
        self.model.aggiungi_visita(visita)

    def rimuovi_visita_by_id(self, id):
        self.model.rimuovi_visita_by_id(id)

    def get_visita_by_id(self, id):
        return self.model.get_visita_by_id(id)

    def get_visita_by_index(self, index):
        return self.model.get_visita_by_index(index)

    def get_lista_visite(self):
        return self.model.get_lista_visite()

    def get_visita_by_codice_fiscale(self, codice_fiscale):
        return self.model.get_visita_by_codice_fiscale(codice_fiscale)

    def save_data(self):
        self.model.save_data()
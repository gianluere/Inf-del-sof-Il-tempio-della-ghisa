from listanutrizionisti.model.ListaNutrizionisti import ListaNutrizionisti


class ControllerListaNutrizionisti():

    def __init__(self):
        self.model = ListaNutrizionisti()

    def aggiungi_nutrizionista(self, nutrizionista):
        self.model.aggiungi_nutrizionista(nutrizionista)

    def get_lista_nutrizionisti(self):
        return self.model.get_lista_nutrizionisti()

    def get_nutrizionista_by_index(self, index):
        return self.model.get_nutrizionista_by_index(index)

    def get_nutrizionista_by_id(self, id):
        return self.model.get_nutrizionista_by_id(id)

    def rimuovi_nutrizionista_by_id(self, id):
        self.model.rimuovi_nutrizionista_by_id(id)

    def save_data(self):
        self.model.save_data()
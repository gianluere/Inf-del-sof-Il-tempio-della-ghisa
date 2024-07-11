from listadiete.model.ListaDiete import ListaDiete

class ControlloreListaDiete():
    def __init__(self):
        self.model = ListaDiete()

    def aggiungi_dieta(self, dieta):
        self.model.aggiungi_dieta(dieta)

    def rimuovi_dieta_by_id(self, id):
        self.model.rimuovi_dieta_by_id(id)

    def get_dieta_by_id(self, id):
        return self.model.get_dieta_by_id(id)

    def get_dieta_by_index(self, index):
        return self.model.get_dieta_by_index(index)

    def get_lista_diete(self):
        return self.model.get_lista_diete()

    def save_data(self):
        self.model.save_data()
from listaclienti.model.ListaClienti import ListaClienti


class ControllerListaClienti():

    def __init__(self):
        self.model = ListaClienti()

    def aggiungi_cliente(self, cliente):
        self.model.aggiungi_cliente(cliente)

    def get_lista_clienti(self):
        return self.model.get_lista_clienti()

    def get_cliente_by_index(self, index):
        return self.model.get_cliente_by_index(index)

    def get_cliente_by_id(self, id):
        return self.model.get_cliente_by_id(id)

    def rimuovi_cliente_by_id(self, id):
        self.model.rimuovi_cliente_by_id(id)

    def save_data(self):
        self.model.save_data()

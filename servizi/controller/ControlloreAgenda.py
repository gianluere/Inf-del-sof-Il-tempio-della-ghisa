class ControlloreAgenda():

    def __init__(self, agenda):
        self.model = agenda

    def get_id_agenda(self):
        return self.model.id

    def get_lista_corsi_cliente(self):
        return self.model.get_lista_corsi_cliente()

    def get_lista_visite_cliente(self):
        return self.model.get_lista_visite_cliente()

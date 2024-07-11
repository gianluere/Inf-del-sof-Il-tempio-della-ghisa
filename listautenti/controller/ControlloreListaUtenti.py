from listautenti.model.ListaUtenti import ListaUtenti


class ControllerListaUtenti():

    def __init__(self):
        self.model = ListaUtenti()

    def aggiungi_utente(self, utente):
        self.model.aggiungi_utente(utente)

    def get_lista_utenti(self):
        return self.model.get_lista_utenti()

    def get_utente_by_index(self, index):
        return self.model.get_utente_by_index(index)

    def get_utente_by_id(self, id):
        return self.model.get_utente_by_id(id)

    def rimuovi_utente_by_id(self, id):
        self.model.rimuovi_utente_by_id(id)

    def save_data(self):
        self.model.save_data()

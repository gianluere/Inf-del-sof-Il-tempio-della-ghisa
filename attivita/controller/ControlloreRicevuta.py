class ControlloreRicevuta():
    def __init__(self, ricevuta):
        self.model = ricevuta

    def get_id_ricevuta(self):
        return self.model.id

    def get_codice_fiscale_ricevuta(self):
        return self.model.codiceFiscale

    def get_data_ricevuta(self):
        return self.model.data

    def get_prezzo_ricevuta(self):
        return self.model.prezzo
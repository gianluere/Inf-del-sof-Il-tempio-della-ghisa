class ControlloreAbbonamento():
    def __init__(self, abbonamento):
        self.model = abbonamento

    def get_id_abbonamento(self):
        return self.model.id

    def get_tipologia_abbonamento(self):
        return self.model.tipologia

    def get_data_inizio_abbonamento(self):
        return self.model.dataInizio

    def get_data_scadenza(self):
        return self.model.dataScadenza

    def get_data_sospensione(self):
        return self.model.dataSospensione

    def get_scaduto(self):
        return self.model.scaduto

    def set_data_sospensione(self, datasos):
        self.model.set_data_sospensione(datasos)

    def set_scaduto(self, valore):
        self.model.set_scaduto(valore)

    def set_data_scadenza(self, datascad):
        self.model.set_data_scadenza(datascad)

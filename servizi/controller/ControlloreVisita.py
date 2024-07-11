class ControlloreVisita():
    def __init__(self, visita):
        self.model = visita

    def get_id_visita(self):
        return self.model.id

    def get_codiceFiscale_visita(self):
        return self.model.codiceFiscale

    def get_data_visita(self):
        return self.model.Data

    def get_ora_visita(self):
        return self.model.ora

    def get_lista_visite(self):
        return self.model.get_lista_visite()

    def get_num_visite(self):
        return self.model.numVisite

    def set_codiceFiscale(self, codiceFiscale):
        self.model.codiceFiscale = codiceFiscale

    def set_data(self, data):
        self.model.data = data

    def set_ora(self, ora):
        self.model.ora = ora

    def verifica_numero_visite(self):
        return self.model.verifica_numero_visita()

    def elimina_visita_by_id(self, id):
        self.model.elimina_visita_by_id(id)
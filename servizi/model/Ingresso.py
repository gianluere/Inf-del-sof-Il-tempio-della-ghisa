from datetime import datetime

from servizi.model.Servizio import Servizio


class Ingresso(Servizio):
    def __init__(self, id, tipo, codiceFiscale, data):
        super(Ingresso, self).__init__(id)
        self.tipo = tipo
        self.codiceFiscale = codiceFiscale
        self.data = datetime.strptime(data, '%d/%m/%Y').date()

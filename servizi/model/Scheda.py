from datetime import datetime

from servizi.model.Servizio import Servizio


class Scheda(Servizio):
    def __init__(self, id):
        super(Scheda, self).__init__(id) #id uguale id cliente



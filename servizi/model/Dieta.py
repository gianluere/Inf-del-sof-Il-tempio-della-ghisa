from servizi.model.Servizio import Servizio


class Dieta(Servizio):
    def __init__(self, id):
        super(Dieta, self).__init__(id)
        #id uguale a id cliente
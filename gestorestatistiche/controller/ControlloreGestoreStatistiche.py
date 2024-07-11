from gestorestatistiche.model.GestoreStatistiche import GestoreStatistiche


class ControlloreGestoreStatistiche():
    def __init__(self):
        self.model = GestoreStatistiche()

    def get_numero_clenti(self):
        return self.model.numero_clienti

    def get_ingressi(self):
        return self.model.ingressi

    def get_fasce_eta(self):
        return self.model.fasce_eta

from servizi.model.Servizio import Servizio
from datetime import datetime

class Visita(Servizio):
    def __init__(self, id, codiceFiscale, data, ora):
        super(Visita, self).__init__(id)
        self.codiceFiscale = codiceFiscale
        self.data = datetime.strptime(data, '%d/%m/%Y').date()
        self.ora = datetime.strptime(ora, '%H:%M').time()
        self.listaVisite = []
        self.numVisite = 0

    def aggiungi_vista(self, visita):
        self.listaVisite.append(visita)
        self.numVisite += 1

    def verifica_numero_visite(self):
        return self.numVisite < 1

    def get_lista_visite(self):
        return self.listaVisite

    def elimina_visita_by_id(self, id):
        def is_selected(iscr):
            if iscr.id == id:
                return True
            return False

        self.listaVisite.remove(list(filter(is_selected, self.listaVisite))[0])
        self.numVisite -= 1



from servizi.model.Servizio import Servizio
from datetime import datetime


class Abbonamento(Servizio):
    def __init__(self, id, tipologia, dataInizio, dataScadenza):
        super(Abbonamento, self).__init__(id)   #per semplicità id_cliente = id_abbonamento
        self.tipologia = tipologia
        self.dataInizio = datetime.strptime(dataInizio, '%d/%m/%Y').date() #.strftime("%d/%m/%Y")
        self.dataScadenza = datetime.strptime(dataScadenza, '%d/%m/%Y').date() #.strftime("%d/%m/%Y")
        self.dataSospensione = None
        self.scaduto = None


    def set_data_sospensione(self, dataSos):
        if dataSos is None:
            self.dataSospensione = None
        else:
            self.dataSospensione = datetime.strptime(dataSos, '%d/%m/%Y').date()

    def set_scaduto(self, valore):
        self.scaduto = valore

    def set_data_scadenza(self, datascad):
        self.dataScadenza = datetime.strptime(datascad, '%d/%m/%Y').date()

    

from datetime import datetime


class Ricevuta():
    def __init__(self, id, codFis, data, prezzo):
        self.id = id
        self.codiceFiscale = codFis
        self.data = datetime.strptime(data, '%d/%m/%Y').date()
        self.prezzo = prezzo
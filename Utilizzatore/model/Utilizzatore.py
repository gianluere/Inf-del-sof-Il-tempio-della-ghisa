from datetime import datetime


class Utilizzatore():
    def __init__(self, id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.codiceFiscale = codiceFiscale
        self.dataNascita = datetime.strptime(dataNascita, '%d/%m/%Y').date() #.strftime("%d/%m/%Y")dataNascita
        self.email = email
        self.telefono = telefono
        self.eta = eta



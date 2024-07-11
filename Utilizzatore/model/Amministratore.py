from Utilizzatore.model.Utilizzatore import Utilizzatore

class Amministratore(Utilizzatore):
    def __init__(self, id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta, permessi):
        super(Amministratore, self).__init__(id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta)
        self.permessi = permessi


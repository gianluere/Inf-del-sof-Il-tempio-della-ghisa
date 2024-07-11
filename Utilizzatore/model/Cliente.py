from Utilizzatore.model.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):
    def __init__(self, id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta):
        super(Cliente, self).__init__(id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta)
        self.abbonato = None
        self.abbonamento = None

    def setAbbonamento(self, abbonamento):
        self.abbonamento = abbonamento
        if abbonamento is not None:
            self.abbonato = True
        else:
            self.abbonato = False

    def getAbbonamento(self):
        #if self.abbonamento.is_scaduto():
        #    self.abbonamento = None
        #    self.abbonato = False
        #    return None
        #else:
        return self.abbonamento

    def getAbbonato(self):
        return self.abbonato

    def setAbbonato(self, abbonato):
        self.abbonato = abbonato

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id == other.id and self.email == other.email  # Confronto in base agli attributi unici
        return False

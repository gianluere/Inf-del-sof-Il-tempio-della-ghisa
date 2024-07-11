from Utilizzatore.model.Utilizzatore import Utilizzatore

class Nutrizionista(Utilizzatore):
    def __init__(self, id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta, licenza):
        super(Nutrizionista, self).__init__(id, nome, cognome, codiceFiscale, dataNascita, email, telefono, eta)
        self.licenza = licenza


    def setLicenza(self, licenza):
        self.licenza = licenza

    def __eq__(self, other):
        if isinstance(other, Nutrizionista):
            return self.id == other.id and self.email == other.email  # Confronto in base agli attributi unici
        return False

from datetime import datetime


class ControlloreAllenatore():
    
    def __init__(self, allenatore):
        self.model = allenatore
    
    def get_nome_allenatore(self):
        return self.model.nome

    def get_id_allenatore(self):
        return self.model.id

    def get_cognome_allenatore(self):
        return self.model.cognome

    def get_codfis_allenatore(self):
        return self.model.codiceFiscale

    def get_email_allenatore(self):
        return self.model.email

    def get_telefono_allenatore(self):
        return self.model.telefono

    def get_eta_allenatore(self):
        return self.model.eta

    def get_dataNascita_allenatore(self):
        return self.model.dataNascita

    def get_licenza_allenatore(self):
        return self.model.licenza

    def set_licenza_allenatore(self, licenza):
        self.model.setLicenza(licenza)

    def set_nome_allenatore(self, nome):
        self.model.nome = nome

    def set_cognome_allenatore(self, cognome):
        self.model.cognome=cognome

    def set_codfis_allenatore(self, codfis):
        self.model.codiceFiscale = codfis

    def set_email_allenatore(self, email):
        self.model.email = email

    def set_telefono_allenatore(self, telefono):
        self.model.telefono = telefono

    def set_dataNascita_allenatore(self, dataNascita):
        self.model.dataNascita = datetime.strptime(dataNascita, '%d/%m/%Y').date()

    def set_eta_allenatore(self, eta):
        self.model.eta = eta
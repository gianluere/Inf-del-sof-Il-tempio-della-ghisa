from datetime import datetime


class ControlloreNutrizionista:
    
    def __init__(self, nutrizionista):
        self.model = nutrizionista
    
    def get_nome_nutrizionista(self):
        return self.model.nome

    def get_id_nutrizionista(self):
        return self.model.id

    def get_cognome_nutrizionista(self):
        return self.model.cognome

    def get_codfis_nutrizionista(self):
        return self.model.codiceFiscale

    def get_email_nutrizionista(self):
        return self.model.email

    def get_telefono_nutrizionista(self):
        return self.model.telefono

    def get_eta_nutrizionista(self):
        return self.model.eta

    def get_dataNascita_nutrizionista(self):
        return self.model.dataNascita

    def get_licenza_nutrizionista(self):
        return self.model.licenza

    def set_licenza_nutrizionista(self, licenza):
        self.model.setLicenza(licenza)

    def set_nome_nutrizionista(self, nome):
        self.model.nome = nome

    def set_cognome_nutrizionista(self, cognome):
        self.model.cognome=cognome

    def set_codfis_nutrizionista(self, codfis):
        self.model.codiceFiscale = codfis

    def set_email_nutrizionista(self, email):
        self.model.email = email

    def set_telefono_nutrizionista(self, telefono):
        self.model.telefono = telefono

    def set_dataNascita_nutrizionista(self, dataNascita):
        self.model.dataNascita = datetime.strptime(dataNascita, '%d/%m/%Y').date()

    def set_eta_nutrizionista(self, eta):
        self.model.eta = eta
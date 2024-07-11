from datetime import datetime


class ControlloreCliente():

    def __init__(self, cliente):
        self.model = cliente

    def get_nome_cliente(self):
        return self.model.nome

    def get_id_cliente(self):
        return self.model.id

    def get_cognome_cliente(self):
        return self.model.cognome

    def get_codfis_cliente(self):
        return self.model.codiceFiscale

    def get_email_cliente(self):
        return self.model.email

    def get_telefono_cliente(self):
        return self.model.telefono

    def get_eta_cliente(self):
        return self.model.eta

    def get_dataNascita_cliente(self):
        return self.model.dataNascita

    def get_abbonamento_cliente(self):
        return self.model.getAbbonamento()

    def get_abbonato_cliente(self):
        return self.model.getAbbonato()

    def set_abbonamento_cliente(self, abbonamento):
        self.model.setAbbonamento(abbonamento)

    def set_abbonato_cliente(self, abbonato):
        self.model.setAbbonato(abbonato)

    def set_nome_cliente(self, nome):
        self.model.nome = nome

    def set_cognome_cliente(self, cognome):
        self.model.cognome=cognome

    def set_codfis_cliente(self, codfis):
        self.model.codiceFiscale = codfis

    def set_email_cliente(self, email):
        self.model.email = email

    def set_telefono_cliente(self, telefono):
        self.model.telefono = telefono

    def set_dataNascita_cliente(self, dataNascita):
        self.model.dataNascita = datetime.strptime(dataNascita, '%d/%m/%Y').date()

    def set_eta_cliente(self, eta):
        self.model.eta = eta
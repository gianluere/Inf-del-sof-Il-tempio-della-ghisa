class ControlloreAmministratore():
    
    def __init__(self, amministratore):
        self.model = amministratore
        
    def get_nome_amministratore(self):
        return self.model.nome

    def get_id_amministratore(self):
        return self.model.id

    def get_cognome_amministratore(self):
        return self.model.cognome

    def get_codfis_amministratore(self):
        return self.model.codiceFiscale

    def get_email_amministratore(self):
        return self.model.email

    def get_telefono_amministratore(self):
        return self.model.telefono

    def get_eta_amministratore(self):
        return self.model.eta

    def get_dataNascita_amministratore(self):
        return self.model.dataNascita
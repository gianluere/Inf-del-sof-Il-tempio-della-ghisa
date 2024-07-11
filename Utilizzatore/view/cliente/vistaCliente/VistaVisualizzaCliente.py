from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from login.model.DeleteDatabase import delete


class VistaVisualizzaCliente(QWidget):
    def __init__(self, cliente, elimina_callback, controllerUtenti, controllerClienti, callback):
        super(VistaVisualizzaCliente, self).__init__()
        uic.loadUi("Utilizzatore/view/cliente/vistaCliente/vistaCliente.ui", self)
        self.controller = ControlloreCliente(cliente)
        self.elimina_callback = elimina_callback
        self.controllerUtenti = controllerUtenti
        self.controllerClienti = controllerClienti
        self.callback = callback
        #print(self.controller.get_dataNascita_cliente().strftime("%d/%m/%Y"))

        self.nome.setText(self.controller.get_nome_cliente())
        self.cognome.setText(self.controller.get_cognome_cliente())
        self.codFiscale.setText(self.controller.get_codfis_cliente())
        self.id.setText(self.controller.get_id_cliente())
        self.dataNascita.setText(self.controller.get_dataNascita_cliente().strftime("%d/%m/%Y"))
        self.eta.setText(self.controller.get_eta_cliente())
        self.telefono.setText(self.controller.get_telefono_cliente())
        self.email.setText(self.controller.get_email_cliente())
        if self.controller.get_abbonato_cliente() and (self.controller.get_abbonamento_cliente() is not None):
            self.checkBox.setChecked(True)
            self.checkBox.setEnabled(False)
            #print(self.controller.get_abbonato_cliente())
            #print(self.controller.get_abbonamento_cliente().dataInizio)
            self.dataInizio.setText(self.controller.get_abbonamento_cliente().dataInizio.strftime("%d/%m/%Y"))
            self.dataScadenza.setText(self.controller.get_abbonamento_cliente().dataScadenza.strftime("%d/%m/%Y"))
        elif self.controller.get_abbonato_cliente() and (self.controller.get_abbonamento_cliente() is None):
            self.checkBox.setChecked(True)
            self.checkBox.setEnabled(False)
            self.dataInizio.setText(self.controller.get_abbonamento_cliente().dataInizio.strftime("%d/%m/%Y"))
            self.dataScadenza.setText("SOSPESO")

        self.button_conferma.hide()


        self.button_elimina.clicked.connect(self.elimina_cliente)
        self.button_modifica.clicked.connect(self.modifica_cliente)
        self.button_conferma.clicked.connect(self.conferma_modifica)


    def elimina_cliente(self):
        self.elimina_callback(self.controller.get_id_cliente())
        self.controllerClienti.save_data()
        self.controllerUtenti.rimuovi_utente_by_id(self.controller.get_id_cliente())
        self.controllerUtenti.save_data()
        delete(self.controller.get_id_cliente())
        self.callback()
        self.close()

    def modifica_cliente(self):
        self.nome.setReadOnly(False)
        self.cognome.setReadOnly(False)
        self.codFiscale.setReadOnly(False)
        self.dataNascita.setReadOnly(False)
        self.eta.setReadOnly(False)
        self.telefono.setReadOnly(False)
        self.email.setReadOnly(False)
        self.button_elimina.setEnabled(False)
        self.button_modifica.setEnabled(False)
        self.button_elimina.hide()
        self.button_modifica.hide()
        self.button_conferma.setEnabled(True)
        self.button_conferma.show()

    def conferma_modifica(self):
        self.nome.setReadOnly(True)
        self.cognome.setReadOnly(True)
        self.codFiscale.setReadOnly(True)
        self.dataNascita.setReadOnly(True)
        self.eta.setReadOnly(True)
        self.telefono.setReadOnly(True)
        self.email.setReadOnly(True)
        self.button_conferma.hide()
        self.button_conferma.setEnabled(False)
        self.button_elimina.show()
        self.button_modifica.show()
        self.button_elimina.setEnabled(True)
        self.button_modifica.setEnabled(True)

        self.controller.set_nome_cliente(self.nome.text())
        self.controller.set_cognome_cliente(self.cognome.text())
        self.controller.set_codfis_cliente(self.codFiscale.text())
        self.controller.set_dataNascita_cliente(self.dataNascita.text())
        self.controller.set_eta_cliente(self.eta.text())
        self.controller.set_telefono_cliente(self.telefono.text())
        self.controller.set_email_cliente(self.email.text())
        self.controllerUtenti.save_data()

        
        cliente_clienti = self.controllerClienti.get_cliente_by_id(self.controller.get_id_cliente())
        controllerCliente_clienti = ControlloreCliente(cliente_clienti)
        controllerCliente_clienti.set_nome_cliente(self.nome.text())
        controllerCliente_clienti.set_cognome_cliente(self.cognome.text())
        controllerCliente_clienti.set_codfis_cliente(self.codFiscale.text())
        controllerCliente_clienti.set_dataNascita_cliente(self.dataNascita.text())
        controllerCliente_clienti.set_eta_cliente(self.eta.text())
        controllerCliente_clienti.set_telefono_cliente(self.telefono.text())
        controllerCliente_clienti.set_email_cliente(self.email.text())
        self.controllerClienti.save_data()
        self.callback()


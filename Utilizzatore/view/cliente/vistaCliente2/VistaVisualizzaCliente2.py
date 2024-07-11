from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from login.model.DeleteDatabase import delete


class VistaVisualizzaCliente2(QWidget):
    def __init__(self, cliente):
        super(VistaVisualizzaCliente2, self).__init__()
        uic.loadUi("Utilizzatore/view/cliente/vistaCliente2/VisualizzaCliente2.ui", self)
        self.controller = ControlloreCliente(cliente)


        self.nome.setText(self.controller.get_nome_cliente())
        self.cognome.setText(self.controller.get_cognome_cliente())
        self.codFiscale.setText(self.controller.get_codfis_cliente())
        self.id.setText(self.controller.get_id_cliente())
        self.dataNascita.setText(self.controller.get_dataNascita_cliente().strftime("%d/%m/%Y"))
        self.eta.setText(self.controller.get_eta_cliente())
        self.telefono.setText(self.controller.get_telefono_cliente())
        self.email.setText(self.controller.get_email_cliente())
        if (self.controller.get_abbonato_cliente()):
            self.checkBox.setChecked(True)
            self.checkBox.setEnabled(False)
            # print(self.controller.get_abbonato_cliente())
            # print(self.controller.get_abbonamento_cliente().dataInizio)
            self.dataInizio.setText(self.controller.get_abbonamento_cliente().dataInizio.strftime("%d/%m/%Y"))
            self.dataScadenza.setText(self.controller.get_abbonamento_cliente().dataScadenza.strftime("%d/%m/%Y"))
        else:
            self.checkBox.setEnabled(False)





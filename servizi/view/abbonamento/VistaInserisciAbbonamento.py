from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listautenti.controller.ControlloreListaUtenti import ControllerListaUtenti
from servizi.model.Abbonamento import Abbonamento


class VistaInserisciAbbonamento(QWidget):
    def __init__(self, controller, callback, salvaAbb, parent=None):
        super(VistaInserisciAbbonamento, self).__init__(parent)
        uic.loadUi('servizi/view/abbonamento/vistaInserisciAbbonamento.ui', self)

        self.controller = controller
        self.callback = callback
        self.salvaAbb = salvaAbb

        self.button_conferma.clicked.connect(self.add_abbonamento)


    def add_abbonamento(self):
        id = self.id.text()
        tipologia = self.tipologia.text()
        dataInizio = self.dataInizio.text()
        dataScadenza = self.dataScadenza.text()
        if id == "" or tipologia == "" or dataInizio == "" or dataScadenza == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                QMessageBox.StandardButton.Ok)
        else:

            self.controller.aggiungi_abbonamento(Abbonamento(id, tipologia, dataInizio, dataScadenza))
            self.salvaAbb()
            self.callback()
            controllerUtenti = ControllerListaUtenti()
            controllerClienteUtenti = ControlloreCliente(controllerUtenti.get_utente_by_id(id))
            controllerClienteUtenti.set_abbonamento_cliente(self.controller.get_abbonamento_by_index(len(self.controller.get_lista_abbonamenti())-1))
            controllerUtenti.save_data()
            controllerClienti = ControllerListaClienti()
            controllerClienteClienti = ControlloreCliente(controllerClienti.get_cliente_by_id(id))
            controllerClienteClienti.set_abbonamento_cliente(self.controller.get_abbonamento_by_index(len(self.controller.get_lista_abbonamenti())-1))
            controllerClienti.save_data()
            self.close()

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.model.Cliente import Cliente
from login.view.inserimentoDatabase.VistaInserisciNelDatabase import VistaInserisciNelDatabase
from login.model.InsertAndGetDatabase import all_key


class VistaInserisciCliente(QWidget):

    def __init__(self, controllerUtenti, callback, controller, salvaCliente, parent=None):
        super(VistaInserisciCliente, self).__init__(parent)
        uic.loadUi('Utilizzatore/view/cliente/vistaInserisciCliente.ui', self)

        self.controllerUtenti = controllerUtenti
        self.callback = callback
        self.controller = controller
        self.salvaCliente = salvaCliente

        self.button_conferma.clicked.connect(self.add_cliente)

    def add_cliente(self):
        ids = all_key()
        id = self.id.text()
        nome = self.nome.text()
        cognome = self.cognome.text()
        cf = self.codiceFiscale.text()
        datanasc = self.dataNascita.text()
        email = self.email.text()
        telefono = self.telefono.text()
        eta = self.eta.text()
        if id == "" or nome == "" or cognome == "" or cf == "" or datanasc == "" or email == "" or telefono == "" or eta == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                 QMessageBox.StandardButton.Ok)
        elif id in ids:
            QMessageBox.critical(self, 'Errore', 'Id già utilizzato',
                                     QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_cliente(Cliente(
                id,
                nome,
                cognome,
                cf,
                datanasc,
                email,
                telefono,
                eta)
            )
            self.salvaCliente()
            self.controllerUtenti.aggiungi_utente(Cliente(
                id,
                nome,
                cognome,
                cf,
                datanasc,
                email,
                telefono,
                eta)
            )
            self.controllerUtenti.save_data()
            self.callback()
            self.vistaInserisciDatabase = VistaInserisciNelDatabase(id, "Cliente")
            self.vistaInserisciDatabase.show()
            self.close()
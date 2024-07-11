from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.model.Nutrizionista import Nutrizionista
from login.view.inserimentoDatabase.VistaInserisciNelDatabase import VistaInserisciNelDatabase
from login.model.InsertAndGetDatabase import all_key


class VistaInserisciNutrizionista(QWidget):

    def __init__(self, controllerUtenti, callback, controller, salvaNutrizionista, parent=None):
        super(VistaInserisciNutrizionista, self).__init__(parent)
        uic.loadUi('Utilizzatore/view/nutrizionista/vistaInserisciNutrizionista.ui', self)
        self.controller = controller
        self.controllerUtenti = controllerUtenti
        self.callback = callback
        self.salvaNutrizionista = salvaNutrizionista

        self.button_conferma.clicked.connect(self.add_nutrizionista)

    def add_nutrizionista(self):
        ids = all_key()
        id = self.id.text()
        nome = self.nome.text()
        cognome = self.cognome.text()
        cf = self.codiceFiscale.text()
        dataNasc = self.dataDiNascita.text()  # cambia con datanasc
        email = self.email.text()
        telefono = self.telefono.text()
        eta = self.eta.text()
        licenza = self.licenza.text()
        if id == "" or nome == "" or cognome == "" or cf == "" or dataNasc == "" or email == "" or telefono == "" or eta == "" or licenza == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                 QMessageBox.StandardButton.Ok)
        elif id in ids:
            QMessageBox.critical(self, 'Errore', 'Id già utilizzato',
                                     QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_nutrizionista(Nutrizionista(
                id,
                nome,
                cognome,
                cf,
                dataNasc,
                email,
                telefono,
                eta,
                licenza)
            )
            self.salvaNutrizionista()
            self.controllerUtenti.aggiungi_utente(Nutrizionista(
                id,
                nome,
                cognome,
                cf,
                dataNasc,
                email,
                telefono,
                eta,
                licenza)
            )
            self.controllerUtenti.save_data()
            self.callback()
            self.vistaInserisciDatabase = VistaInserisciNelDatabase(id, "Nutrizionista")
            self.vistaInserisciDatabase.show()
            self.close()

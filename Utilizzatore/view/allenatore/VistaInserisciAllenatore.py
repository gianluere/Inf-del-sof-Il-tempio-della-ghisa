from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.model.Allenatore import Allenatore
from login.view.inserimentoDatabase.VistaInserisciNelDatabase import VistaInserisciNelDatabase
from login.model.InsertAndGetDatabase import all_key

class VistaInserisciAllenatore(QWidget):

    def __init__(self, controllerUtenti, callback, controller, salvaAllenatore, parent=None):
        super(VistaInserisciAllenatore, self).__init__(parent)
        uic.loadUi('Utilizzatore/view/allenatore/vistaInserisciAllenatore.ui', self)
        self.controller = controller
        self.controllerUtenti = controllerUtenti
        self.callback = callback
        self.salvaAllenatore = salvaAllenatore

        self.button_conferma.clicked.connect(self.add_allenatore)

    def add_allenatore(self):
        ids = all_key() #devo controllare se l'id è già utilizzato
        id = self.id.text()
        nome = self.nome.text()
        cognome = self.cognome.text()
        cf = self.codiceFiscale.text()
        dataNasc = self.dataDiNascita.text() #cambia con datanasc
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
            self.controller.aggiungi_allenatore(Allenatore(
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
            self.salvaAllenatore()
            self.controllerUtenti.aggiungi_utente(Allenatore(
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
            self.vistaInserisciDatabase = VistaInserisciNelDatabase(id, "Allenatore")
            self.vistaInserisciDatabase.show()
            self.close()

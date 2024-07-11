from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from servizi.model.Corso import Corso

class VistaInserisciCorso(QWidget):
    def __init__(self, controller, callback, salvaCorso, parent=None):
        super(VistaInserisciCorso, self).__init__(parent)
        uic.loadUi('servizi/view/corso/view/vistaInserisciCorso.ui', self)
        self.controller = controller
        self.callback = callback
        self.salvaCorso = salvaCorso

        self.button_conferma.clicked.connect(self.add_corso)


    def add_corso(self):
        id = self.id.text()
        tipo = self.tipo.text()
        if id == "" or tipo == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_corso(Corso(id, tipo))
            self.salvaCorso()
            self.callback()
            self.close()



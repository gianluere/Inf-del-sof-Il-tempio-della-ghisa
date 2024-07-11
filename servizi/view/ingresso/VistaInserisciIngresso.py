import os
import shutil

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox

from listaingressi.controller.ControlloreListaIngressi import ControlloreListaIngressi
from servizi.model.Ingresso import Ingresso
from servizi.model.Scheda import Scheda


class VistaInserisciIngresso(QWidget):
    def __init__(self, home, controller, callback, salvaIngresso, parent=None):
        super(VistaInserisciIngresso, self).__init__(parent)
        uic.loadUi('servizi/view/ingresso/vistaInserisciIngresso.ui', self)
        self.controller = controller
        self.callback = callback
        self.salvaIngresso = salvaIngresso
        self.home = home

        self.button_conferma.clicked.connect(self.add_ingresso)


    def add_ingresso(self):
        id = self.id.text()
        if self.abbonato.isChecked():
            tipo = "con"
        else:
            tipo = "senza"
        codiceFiscale = self.codiceFiscale.text()
        data = self.data.text()

        if id == "" or data == "" or codiceFiscale == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                 QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_ingresso(Ingresso(id, tipo, codiceFiscale, data))
            self.salvaIngresso()
            self.callback()
            self.close()

    def closeEvent(self, event):
        self.home.show()


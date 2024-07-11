from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from attivita.model.Ricevuta import Ricevuta


class VistaInserisciRicevuta(QWidget):
    def __init__(self, controller, callback, salvaRic, parent=None):
        super(VistaInserisciRicevuta, self).__init__(parent)
        uic.loadUi('attivita/view/ricevuta/vistaInserisciRicevuta.ui', self)

        self.controller = controller
        self.callback = callback
        self.salvaRic = salvaRic

        self.button_conferma.clicked.connect(self.add_ricevuta)


    def add_ricevuta(self):
        id = self.id.text()
        codiceFiscale = self.codiceFiscale.text()
        data = self.data.text()
        prezzo = self.prezzo.text()
        if id == "" or codiceFiscale == "" or data == "" or prezzo == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                 QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_ricevuta(Ricevuta(id, codiceFiscale, data, prezzo))
            self.salvaRic()
            self.callback()
            self.close()

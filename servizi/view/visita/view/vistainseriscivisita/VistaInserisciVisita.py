from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from servizi.model.Visita import Visita

class VistaInserisciVisita(QWidget):
    def __init__(self, controller, callback, salvaVisita, parent=None):
        super(VistaInserisciVisita, self).__init__(parent)
        uic.loadUi('servizi/view/visita/view/vistainseriscivisita/inserisciVisita.ui', self)
        self.controller = controller
        self.callback = callback
        self.salvaVisita = salvaVisita

        self.button_conferma.clicked.connect(self.add_visita)


    def add_visita(self):
        id = self.id.text()
        codiceFiscale = self.codiceFiscale.text()
        data = self.data.text()
        ora = self.ora.text()
        if id == "" or codiceFiscale == "" or data == "" or ora == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                QMessageBox.StandardButton.Ok)
        else:
            self.controller.aggiungi_visita(Visita(id, codiceFiscale, data, ora))
            self.salvaVisita()
            self.callback()
            self.close()

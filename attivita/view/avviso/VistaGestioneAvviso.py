from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from attivita.model.Avviso import Avviso


class VistaGestioneAvviso(QWidget):
    def __init__(self, home):
        super(VistaGestioneAvviso, self).__init__()
        uic.loadUi("attivita/view/avviso/GestioneAvvisi.ui", self)
        self.home = home

        self.button_invia.clicked.connect(self.send)

    def send(self):
        avv = Avviso(self.to.text(), self.subject.text(), self.body.text())
        avv.send_avviso()
        self.home.show()
        self.close()

    def closeEvent(self, event):
        self.home.show()
        self.close()

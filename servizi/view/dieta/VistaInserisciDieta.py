import os
import shutil

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog

from listadiete.controller.ControlloreListaDiete import ControlloreListaDiete
from servizi.model.Dieta import Dieta

class VistaInserisciDieta(QWidget):
    def __init__(self, home, parent=None):
        super(VistaInserisciDieta, self).__init__(parent)
        uic.loadUi("servizi/view/dieta/GestioneDiete.ui", self)
        self.home = home
        self.controller = ControlloreListaDiete()
        self.button_selezionaFile.clicked.connect(self.add_dieta)

    def add_dieta(self):
        id = self.id.text()
        file_selezionato, _ = QFileDialog.getOpenFileName(self, "Seleziona file", "", "All Files (*)", "",
                                                              QFileDialog().options().DontUseNativeDialog)
        if file_selezionato:
            #print(file_selezionato)
            # Apre una finestra di dialogo per selezionare una cartella di destinazione
            #cartella_destinazione = QFileDialog.getExistingDirectory(None, "Seleziona cartella di destinazione", "",
                                                                     #QFileDialog().options().DontUseNativeDialog)
            cartella_destinazione = os.path.dirname('listadiete/pdf/')
            #if cartella_destinazione:
            shutil.copy(file_selezionato, cartella_destinazione)

        if self.controller.get_dieta_by_id(id) is None:
            self.controller.aggiungi_dieta(Dieta(id))
            self.controller.save_data()
        self.close()

    def closeEvent(self, event):
        self.home.show()
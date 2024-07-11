import os
import shutil

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox

from listaschede.controller.ControlloreListaSchede import ControlloreListaSchede
from servizi.model.Scheda import Scheda


class VistaInserisciScheda(QWidget):
    def __init__(self, home, parent=None):
        super(VistaInserisciScheda, self).__init__(parent)
        uic.loadUi('servizi/view/scheda/GestioneSchede.ui', self)
        self.home = home
        self.controller = ControlloreListaSchede()
        self.button_selezionaFile.clicked.connect(self.add_scheda)

    def add_scheda(self):
        id = self.id.text()
        file_selezionato, _ = QFileDialog.getOpenFileName(self, "Seleziona file", "", "All Files (*)", "",
                                                          QFileDialog().options().DontUseNativeDialog)
        if file_selezionato:
            #print(file_selezionato)
            # Apre una finestra di dialogo per selezionare una cartella di destinazione
            #cartella_destinazione = QFileDialog.getExistingDirectory(None, "Seleziona cartella di destinazione", "",
                                                                     #QFileDialog().options().DontUseNativeDialog)
            cartella_destinazione = os.path.dirname('listaschede/pdf/')
            #if cartella_destinazione:
            shutil.copy(file_selezionato, cartella_destinazione)
        if self.controller.get_scheda_by_id(id) is None:
            self.controller.aggiungi_scheda(Scheda(id))
            self.controller.save_data()
        self.close()

    def closeEvent(self, event):
        self.home.show()


        

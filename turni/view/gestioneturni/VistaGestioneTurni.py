import os
import shutil
import sys

from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox


class VistaGestioneTurni(QWidget):
    def __init__(self, home, parent=None):
        super(VistaGestioneTurni, self).__init__(parent)
        self.home = home
        file_selezionato, _ = QFileDialog.getOpenFileName(self, "Seleziona file", "", "All Files (*)", "",
                                                          QFileDialog().options().DontUseNativeDialog)
        if file_selezionato:
            print(file_selezionato)
            # Apre una finestra di dialogo per selezionare una cartella di destinazione
            cartella_destinazione = QFileDialog.getExistingDirectory(None, "Seleziona cartella di destinazione", "",
                                                                     QFileDialog().options().DontUseNativeDialog)
            if cartella_destinazione:
                # print(cartella_destinazione)
                # nome_file = os.path.basename(file_selezionato)
                # print(nome_file)

                # Sposta il file nella cartella di destinazione
                # os.replace(file_selezionato, os.path.join(cartella_destinazione, nome_file))
                shutil.copy(file_selezionato, cartella_destinazione)
                #self.close()

            else:
                QMessageBox.critical(self, 'Errore', 'Cartella non selezionata', QMessageBox.StandardButton.Ok)
                self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'File non selezionato', QMessageBox.StandardButton.Ok)
            self.close()
        #self.chiudi()

    def chiudi(self):
        self.close()

    def closeEvent(self, event):
        self.home.show()


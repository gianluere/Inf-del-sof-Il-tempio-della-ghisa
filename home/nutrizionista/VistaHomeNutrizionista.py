import os
import subprocess
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.controller.ControlloreNutrizionista import ControlloreNutrizionista
from listaclienti.view.VistaListaClienti import VistaListaClienti
from listanutrizionisti.controller.ControlloreListaNutrizionisti import ControllerListaNutrizionisti
from servizi.view.dieta.VistaInserisciDieta import VistaInserisciDieta
from listavisite.view.VistaListaVisite import VistaListaVisite


class VistaHomeNutrizionista(QWidget):
    def __init__(self, login, utente, parent=None):
        super(VistaHomeNutrizionista, self).__init__(parent)
        uic.loadUi('home/nutrizionista/vistaHomeNutrizionista.ui', self)
        self.login = login
        self.controller = ControlloreNutrizionista(ControllerListaNutrizionisti().get_nutrizionista_by_id(utente))

        self.button_visualizzaClienti.clicked.connect(self.go_gest_clienti)
        self.button_gestDieta.clicked.connect(self.go_gest_diete)
        self.button_logout.clicked.connect(self.go_logout)
        self.button_gestVisite.clicked.connect(self.go_gest_visite)
        self.button_visualizzaTurni.clicked.connect(self.go_vista_turni)

    def go_gest_visite(self):
        self.hide()
        self.vistaListaVisite = VistaListaVisite(self)
        self.vistaListaVisite.show()

    def go_vista_turni(self):
        directory = "turni/turni.pdf"
        dire = Path(directory).resolve()
        if os.name == "posix":

            apertura = subprocess.Popen(["open", dire])
            # subprocess.Popen(["open", directory])

            codice_uscita = apertura.wait()

            # Verifica il codice di uscita per vedere se esiste o meno la scheda relativa al cliente
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Turni non disponibili', QMessageBox.StandardButton.Ok)
        else:
            apertura = subprocess.Popen([dire], shell=True)
            codice_uscita = apertura.wait()
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Turni non disponibili', QMessageBox.StandardButton.Ok)


    def go_gest_diete(self):
        self.hide()
        self.vistaInserisciDieta = VistaInserisciDieta(self)
        self.vistaInserisciDieta.show()

    def go_gest_clienti(self):
        self.hide()
        self.vistaListaClienti = VistaListaClienti(self, "nutrizionista")
        self.vistaListaClienti.show()


    def go_logout(self):
        self.close()
        self.login.username.setText("")
        self.login.password.setText("")
        self.login.show()
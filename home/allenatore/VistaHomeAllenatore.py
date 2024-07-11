import os
import subprocess
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.controller.ControlloreAllenatore import ControlloreAllenatore
from listaallenatori.controller.ControlloreListaAllenatori import ControllerListaAllenatori
from listaclienti.view.VistaListaClienti import VistaListaClienti
from listacorsi.view.gestionecorsiallenatore.view.VistaListaCorsiAllenatore import VistaListaCorsiAllenatore
from servizi.view.scheda.VistaInserisciScheda import VistaInserisciScheda
from turni.view.gestioneturni.VistaGestioneTurni import VistaGestioneTurni


class VistaHomeAllenatore(QWidget):
    def __init__(self, login, utente, parent=None):
        super(VistaHomeAllenatore, self).__init__(parent)
        uic.loadUi('home/allenatore/vistaHomeAllenatore.ui', self)
        self.login = login
        self.controller = ControlloreAllenatore(ControllerListaAllenatori().get_allenatore_by_id(utente))

        self.button_gestIscritti.clicked.connect(self.go_gestione_iscritti_corso)
        self.button_gestSchede.clicked.connect(self.go_gestione_schede)
        self.button_visualizzaCliente.clicked.connect(self.go_gest_clienti)
        self.button_visualizzaTurni.clicked.connect(self.go_vista_turni)
        self.button_logout.clicked.connect(self.go_logout)



    def go_gestione_iscritti_corso(self):
        self.hide()
        self.vistaIscrittiCorso = VistaListaCorsiAllenatore(self)
        self.vistaIscrittiCorso.show()

    def go_gestione_schede(self):
        self.hide()
        self.vistaInserisciScheda = VistaInserisciScheda(self)
        self.vistaInserisciScheda.show()


    def go_gest_clienti(self):
        self.hide()
        self.vistaListaClienti = VistaListaClienti(self, "allenatore")
        self.vistaListaClienti.show()

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

    def go_logout(self):
        self.close()
        self.login.username.setText("")
        self.login.password.setText("")
        self.login.show()

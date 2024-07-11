import os
import subprocess
from pathlib import Path
from datetime import datetime

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from attivita.model.Avviso import Avviso
from listaabbonamenti.controller.ControlloreListaAbbonamenti import ControlloreListaAbbonamenti
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from servizi.controller.ControlloreAbbonamento import ControlloreAbbonamento
from servizi.view.agenda.VistaVisualizzaAgenda import VistaVisualizzaAgenda


class VistaHomeCliente(QWidget):
    def __init__(self, login, id_cliente, parent=None):
        super(VistaHomeCliente, self).__init__(parent)
        uic.loadUi('home/cliente/vistaHomeCliente.ui', self)
        self.login = login
        self.controller = ControlloreCliente(ControllerListaClienti().get_cliente_by_id(id_cliente))

        self.button_visualizzaScheda.clicked.connect(self.show_scheda)
        self.button_visualizzaDieta.clicked.connect(self.show_dieta)
        self.button_logout.clicked.connect(self.go_logout)
        self.button_visualizzaAgenda.clicked.connect(self.go_show_agenda)
        self.button_richiestaSospensioneAbbonamento.clicked.connect(self.richiedi_sosp_abb)

    def show_scheda(self):
        directory = "listaschede/pdf/"+self.controller.get_codfis_cliente()+".pdf"
        dire = Path(directory).resolve()
        if os.name == "posix":

            apertura = subprocess.Popen(["open", dire])
            # subprocess.Popen(["open", directory])

            codice_uscita = apertura.wait()

            # Verifica il codice di uscita per vedere se esiste o meno la scheda relativa al cliente
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Scheda non disponibile', QMessageBox.StandardButton.Ok)
        else:
            apertura = subprocess.Popen([dire], shell=True)
            codice_uscita = apertura.wait()
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Scheda non disponibile', QMessageBox.StandardButton.Ok)

    def show_dieta(self):
        directory = "listadiete/pdf/" + self.controller.get_codfis_cliente() + ".pdf"
        dire = Path(directory).resolve()
        if os.name == "posix":

            apertura = subprocess.Popen(["open", dire])
            # subprocess.Popen(["open", directory])

            codice_uscita = apertura.wait()

            # Verifica il codice di uscita per vedere se esiste o meno la scheda relativa al cliente
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Dieta non disponibile', QMessageBox.StandardButton.Ok)
        else:
            apertura = subprocess.Popen([dire], shell=True)
            codice_uscita = apertura.wait()
            if codice_uscita != 0:
                QMessageBox.critical(self, 'Errore', 'Dieta non disponibile', QMessageBox.StandardButton.Ok)

    def go_show_agenda(self):
        self.hide()
        self.VistaVisualizzaAgenda = VistaVisualizzaAgenda(self, self.controller)
        self.VistaVisualizzaAgenda.show()


    def richiedi_sosp_abb(self):

        if self.controller.get_abbonamento_cliente() is not None:
            if self.controller.get_abbonamento_cliente().tipologia == 'Annuale':
                mess = 'Il cliente con id = ' + self.controller.get_id_cliente() + ", " + self.controller.get_nome_cliente() + " " + self.controller.get_cognome_cliente() + " ha richiesto la sospensione dell'abbonamento"
                avv = Avviso('ingdelsof@gmail.com', 'Richiesta sospensione abbonamento', mess)
                avv.send_avviso()
                QMessageBox.warning(self, 'Attenzione', 'Richiesta sospensione abbonamento inviata',
                                    QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.warning(self, 'Attenzione', "E' possibile sospendere solo l'annuale",
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, 'Attenzione', 'Non sei abbonato',QMessageBox.StandardButton.Ok)


    def go_logout(self):
        self.close()
        self.login.username.setText("")
        self.login.password.setText("")
        self.login.show()



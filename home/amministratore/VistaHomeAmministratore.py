import os
import shutil
import sys

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PyQt6 import uic
import matplotlib
matplotlib.use('QtAgg')  # Usa il backend TkAgg per le finestre indipendenti
import matplotlib.pyplot as plt
import seaborn as sns

from attivita.view.avviso.VistaGestioneAvviso import VistaGestioneAvviso
from gestorestatistiche.controller.ControlloreGestoreStatistiche import ControlloreGestoreStatistiche
#import pygame

from listaabbonamenti.view.VistaListaAbbonamenti import VistaListaAbbonamenti
from listaingressi.view.VistaListaIngressi import VistaListaIngressi
from listaricevute.view.VistaListaRicevute import VistaListaRicevute
from listautenti.view.VistaListaUtenti import VistaListaUtenti
from listacorsi.view.VistaListaCorsi import VistaListaCorsi
from turni.view.gestioneturni.VistaGestioneTurni import VistaGestioneTurni


class VistaHomeAmministratore(QWidget):
    def __init__(self, login, parent=None):
        super(VistaHomeAmministratore, self).__init__(parent)
        uic.loadUi('home/amministratore/vistaHomeAmministratore.ui', self)
        self.login = login

        self.button_gestUtenti.clicked.connect(self.go_gest_utenti)
        self.button_gestCorsi.clicked.connect(self.go_gest_corsi)
        self.button_gestAbbonamenti.clicked.connect(self.go_gest_abbonamenti)
        self.button_gestRicevute.clicked.connect(self.go_gest_ricevute)
        self.button_logout.clicked.connect(self.go_logout)
        self.button_gestTurni.clicked.connect(self.go_gest_turni)
        self.button_gestIngressi.clicked.connect(self.go_gest_ingressi)
        self.button_gestAvvisi.clicked.connect(self.go_gest_avvisi)
        self.button_stats.clicked.connect(self.go_statistiche)

    def go_gest_utenti(self):
        self.hide()
        self.vistaListaUtenti = VistaListaUtenti(self)
        self.vistaListaUtenti.show()

    def go_gest_corsi(self):
        self.hide()
        self.vistaListaCorsi = VistaListaCorsi(self)
        self.vistaListaCorsi.show()

    def go_gest_abbonamenti(self):
        self.hide()
        self.vistaListaAbbonamenti = VistaListaAbbonamenti(self)
        self.vistaListaAbbonamenti.show()

    def go_gest_ricevute(self):
        self.hide()
        self.vistaListaRicevute = VistaListaRicevute(self)
        self.vistaListaRicevute.show()

    def go_gest_ingressi(self):
        self.hide()
        self.vistaListaIngressi = VistaListaIngressi(self)
        self.vistaListaIngressi.show()


    def go_gest_turni(self):
        # self.hide()
        f = 0
        # self.vistaGestioneTurni = VistaGestioneTurni(self)
        # self.vistaGestioneTurni.show()

        a = QFileDialog()

        file_selezionato, _ = a.getOpenFileName(None, "Seleziona file", "", "All Files (*)", "",
                                                a.options().DontUseNativeDialog)
        if file_selezionato:
            print(file_selezionato)

            # Apre una finestra di dialogo per selezionare una cartella di destinazione
            #cartella_destinazione = a.getExistingDirectory(None, "Seleziona cartella di destinazione", "",
            #                                               a.options().DontUseNativeDialog)
            cartella_destinazione = os.path.dirname('turni/')
            a.close()

            if cartella_destinazione:
                print(cartella_destinazione)
                nome_file = os.path.basename(file_selezionato)

                print(nome_file)

                # Sposta il file nella cartella di destinazione
                # os.replace(file_selezionato, os.path.join(cartella_destinazione, nome_file))
                shutil.copy(file_selezionato, cartella_destinazione)
            else:

                # QMessageBox.critical(self, 'Errore', 'Cartella non selezionata', QMessageBox.StandardButton.Ok)
                f = 1
        else:
            # QMessageBox.critical(self, 'Errore', 'File non selezionato', QMessageBox.StandardButton.Ok)
            f = 2
        # self.show()

        #if f == 1:
        #    QMessageBox.critical(self, 'Errore', 'Cartella non selezionata', QMessageBox.StandardButton.Ok)
        #elif f == 2:
        #    QMessageBox.critical(self, 'Errore', 'File non selezionato', QMessageBox.StandardButton.Ok)
        #else:
        #    QMessageBox.critical(self, 'Ok', 'File spostato correttamente', QMessageBox.StandardButton.Ok)

        # self.mostra_schermata(f)


        self.mostra_schermata(f)

    def mostra_schermata(self, a):
        if a == 1:

            QMessageBox.critical(QMessageBox(), 'Errore', 'cartella non selezionata', QMessageBox.StandardButton.Ok)
            # QMessageBox.critical(QMessageBox(), 'Errore', 'cartella non selezionata', QMessageBox.StandardButton.Ok)
            # QMessageBox.critical(self, 'Errore', 'Cartella non selezionata', QMessageBox.StandardButton.Ok)
        elif a == 2:
            # QMessageBox.critical(QMessageBox(), 'Errore', 'file non selezionato', QMessageBox.StandardButton.Ok)
            QMessageBox.critical(QMessageBox(), 'Errore', 'file non selezionato', QMessageBox.StandardButton.Ok)
            # QMessageBox.critical(self, 'Errore', 'File non selezionato', QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(self, 'Ok', 'File spostato correttamente', QMessageBox.StandardButton.Ok)


    def go_gest_avvisi(self):
        self.hide()
        self.vistaGestioneAvviso = VistaGestioneAvviso(self)
        self.vistaGestioneAvviso.show()

    def go_statistiche(self):
        controller = ControlloreGestoreStatistiche()

        # define data
        ingressi = controller.get_ingressi()
        if ingressi[0] != 0 or ingressi[1] != 0:
            labels = ['Con abbonamento', 'Senza abbonamento']


            # define Seaborn color palette to use
            colors = sns.color_palette('bright')[0:2]
            label_colors = [f'{label} ({color})' for label, color in zip(labels, colors)]

            # create pie chart
            plt.figure().canvas.manager.set_window_title('Distribuzione degli ingressi')
            plt.pie(ingressi, labels=labels, colors=colors, autopct='%.0f%%')
            plt.title('Distribuzione degli ingressi')
            plt.show()
        else:
            QMessageBox.critical(QMessageBox(), 'Attenzione', "Nessun ingresso presente all'interno dei dati", QMessageBox.StandardButton.Ok)

        numero_clienti = controller.get_numero_clenti()
        fasce_eta = controller.get_fasce_eta()
        plt.figure().canvas.manager.set_window_title('Distribuzione dei clienti per fascia di età')  # Create a new figure
        plt.bar(fasce_eta, numero_clienti, color='blue')
        plt.xlabel('Fascia di età')
        plt.ylabel('Numero di clienti')
        plt.title('Distribuzione dei clienti per fascia di età')
        plt.ylim(0, max(numero_clienti) + 5)
        plt.show()



    def go_logout(self):
        self.close()
        self.login.username.setText("")
        self.login.password.setText("")
        self.login.show()

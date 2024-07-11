import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox

from login.model.InsertAndGetDatabase import *


class VistaInserisciNelDatabase(QWidget):

    def __init__(self, chiave, tipe, parent=None):
        super(VistaInserisciNelDatabase, self).__init__(parent)
        uic.loadUi('login/view/inserimentoDatabase/vistaInserisciDatabase.ui', self)
        self.chiave = chiave
        self.tipe = tipe

        self.id.setText(self.chiave)
        self.id.setReadOnly(True)

        self.tipologia.setText(self.tipe)
        self.tipologia.setReadOnly(True)


        self.button_conferma.clicked.connect(self.add_utente)

    def add_utente(self):

        username = self.username.text()
        password = self.password.text()
        if username == "" or password == "":
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste!!!',
                                 QMessageBox.StandardButton.Ok)
        elif len(password) < 6:
            QMessageBox.critical(self, 'Errore', 'La password deve avere almeno 6 caratteri',
                                     QMessageBox.StandardButton.Ok)
        else:
            usernames = all_username()
            if username in usernames:
                QMessageBox.critical(self, 'Errore', 'Username già utilizzato',
                                     QMessageBox.StandardButton.Ok)
            else:
                insert(self.chiave, username, password, self.tipe)
                self.close()

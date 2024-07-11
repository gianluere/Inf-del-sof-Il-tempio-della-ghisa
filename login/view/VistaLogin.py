from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
import socket
import time


from home.allenatore.VistaHomeAllenatore import VistaHomeAllenatore
from home.amministratore.VistaHomeAmministratore import VistaHomeAmministratore
from home.cliente.VistaHomeCliente import VistaHomeCliente
from home.nutrizionista.VistaHomeNutrizionista import VistaHomeNutrizionista


class VistaLogin(QWidget):

    def __init__(self, backup, server, avvisi, parent=None):
        super(VistaLogin, self).__init__(parent)
        self.backup = backup
        self.server = server
        self.avvisi = avvisi
        uic.loadUi('login/view/login.ui', self)

        self.button_login.clicked.connect(self.verifica)

    def verifica(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 63001))
        user = self.username.text()
        passw = self.password.text()

        if (user == "" or passw == ""):
            QMessageBox.critical(self, 'Errore', 'Username o password non corretta', QMessageBox.StandardButton.Ok)
            self.username.setText("")
            self.password.setText("")
        else:



            client.send(user.encode())
            time.sleep(0.1)
            client.send(passw.encode())

            mess = client.recv(1024).decode()



            if mess == "Login failed":
                QMessageBox.critical(self, 'Errore', 'Username o password non corretta', QMessageBox.StandardButton.Ok)
                self.username.setText("")
                self.password.setText("")
            else:
                if mess == "Amministratore":
                    self.hide()
                    self.vistaHomeAmministratore = VistaHomeAmministratore(self)
                    self.vistaHomeAmministratore.show()
                elif mess == "Cliente":
                    self.hide()
                    utente = client.recv(1024).decode()
                    self.vistaHomeCliente = VistaHomeCliente(self, utente)
                    self.vistaHomeCliente.show()
                elif mess == "Allenatore":
                    self.hide()
                    utente = client.recv(1024).decode()
                    self.vistaHomeAllenatore = VistaHomeAllenatore(self, utente)
                    self.vistaHomeAllenatore.show()
                elif mess == "Nutrizionista":
                    self.hide()
                    utente = client.recv(1024).decode()
                    self.vistaHomeNutrizionista = VistaHomeNutrizionista(self, utente)
                    self.vistaHomeNutrizionista.show()

    def closeEvent(self, event):
        self.backup.terminate()
        self.server.terminate()
        self.avvisi.terminate()

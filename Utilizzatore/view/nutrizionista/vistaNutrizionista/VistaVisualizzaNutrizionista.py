from PyQt6 import uic
from PyQt6.QtWidgets import QWidget


from Utilizzatore.controller.ControlloreNutrizionista import ControlloreNutrizionista
from login.model.DeleteDatabase import delete


class VistaVisualizzaNutrizionista(QWidget):
    def __init__(self, nutrizionista, elimina_callback, controllerUtenti, controllerNutrizionisti, callback):
        super(VistaVisualizzaNutrizionista, self).__init__()
        uic.loadUi("Utilizzatore/view/nutrizionista/vistaNutrizionista/vistaVisualizzaNutrizionista.ui", self)
        self.controller = ControlloreNutrizionista(nutrizionista)
        self.elimina_callback = elimina_callback
        self.controllerUtenti = controllerUtenti
        self.controllerNutrizionisti = controllerNutrizionisti
        self.callback = callback

        self.nome.setText(self.controller.get_nome_nutrizionista())
        self.cognome.setText(self.controller.get_cognome_nutrizionista())
        self.codiceFiscale.setText(self.controller.get_codfis_nutrizionista())
        self.id.setText(self.controller.get_id_nutrizionista())
        self.dataDiNascita.setText(self.controller.get_dataNascita_nutrizionista().strftime("%d/%m/%Y"))
        self.eta.setText(self.controller.get_eta_nutrizionista())
        self.telefono.setText(self.controller.get_telefono_nutrizionista())
        self.email.setText(self.controller.get_email_nutrizionista())
        self.licenza.setText(self.controller.get_licenza_nutrizionista())
        self.button_conferma.hide()

        self.button_elimina.clicked.connect(self.elimina_nutrizionista)
        self.button_modifica.clicked.connect(self.modifica_nutrizionista)
        self.button_conferma.clicked.connect(self.conferma_modifica)

    def elimina_nutrizionista(self):
        self.elimina_callback(self.controller.get_id_nutrizionista())
        self.controllerNutrizionisti.save_data()
        self.controllerUtenti.rimuovi_utente_by_id(self.controller.get_id_nutrizionista())
        self.controllerUtenti.save_data()
        delete(self.controller.get_id_nutrizionista())
        self.callback()
        self.close()

    def modifica_nutrizionista(self):
        self.nome.setReadOnly(False)
        self.cognome.setReadOnly(False)
        self.codiceFiscale.setReadOnly(False)
        self.dataDiNascita.setReadOnly(False)
        self.eta.setReadOnly(False)
        self.telefono.setReadOnly(False)
        self.email.setReadOnly(False)
        self.licenza.setReadOnly(False)
        self.button_elimina.setEnabled(False)
        self.button_modifica.setEnabled(False)
        self.button_elimina.hide()
        self.button_modifica.hide()
        self.button_conferma.setEnabled(True)
        self.button_conferma.show()

    def conferma_modifica(self):
        self.nome.setReadOnly(True)
        self.cognome.setReadOnly(True)
        self.codiceFiscale.setReadOnly(True)
        self.dataDiNascita.setReadOnly(True)
        self.eta.setReadOnly(True)
        self.telefono.setReadOnly(True)
        self.email.setReadOnly(True)
        self.licenza.setReadOnly(True)
        self.button_conferma.hide()
        self.button_conferma.setEnabled(False)
        self.button_elimina.show()
        self.button_modifica.show()
        self.button_elimina.setEnabled(True)
        self.button_modifica.setEnabled(True)

        self.controller.set_nome_nutrizionista(self.nome.text())
        self.controller.set_cognome_nutrizionista(self.cognome.text())
        self.controller.set_codfis_nutrizionista(self.codiceFiscale.text())
        self.controller.set_dataNascita_nutrizionista(self.dataDiNascita.text())
        self.controller.set_eta_nutrizionista(self.eta.text())
        self.controller.set_telefono_nutrizionista(self.telefono.text())
        self.controller.set_email_nutrizionista(self.email.text())
        self.controller.set_licenza_nutrizionista(self.licenza.text())
        self.controllerUtenti.save_data()

        # recuperare bene elemento dalla lista clienti (sbagliato)

        nutrizionista_nutrizionisti = self.controllerNutrizionisti.get_nutrizionista_by_id(self.controller.get_id_nutrizionista())
        controllerNutrizionista_nutrizionisti = ControlloreNutrizionista(nutrizionista_nutrizionisti)
        controllerNutrizionista_nutrizionisti.set_nome_nutrizionista(self.nome.text())
        controllerNutrizionista_nutrizionisti.set_cognome_nutrizionista(self.cognome.text())
        controllerNutrizionista_nutrizionisti.set_codfis_nutrizionista(self.codiceFiscale.text())
        controllerNutrizionista_nutrizionisti.set_dataNascita_nutrizionista(self.dataDiNascita.text())
        controllerNutrizionista_nutrizionisti.set_eta_nutrizionista(self.eta.text())
        controllerNutrizionista_nutrizionisti.set_telefono_nutrizionista(self.telefono.text())
        controllerNutrizionista_nutrizionisti.set_email_nutrizionista(self.email.text())
        controllerNutrizionista_nutrizionisti.set_licenza_nutrizionista(self.licenza.text())
        self.controllerNutrizionisti.save_data()
        self.callback()





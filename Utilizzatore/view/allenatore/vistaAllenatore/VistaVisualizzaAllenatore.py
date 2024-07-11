from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from Utilizzatore.controller.ControlloreAllenatore import ControlloreAllenatore
from login.model.DeleteDatabase import delete


class VistaVisualizzaAllenatore(QWidget):
    def __init__(self, allenatore, elimina_callback, controllerUtenti, controllerAllenatori, callback):
        super(VistaVisualizzaAllenatore, self).__init__()
        uic.loadUi("Utilizzatore/view/allenatore/vistaAllenatore/vistaVisualizzaAllenatore.ui", self)
        self.controller = ControlloreAllenatore(allenatore)
        self.elimina_callback = elimina_callback
        self.controllerUtenti = controllerUtenti
        self.controllerAllenatori = controllerAllenatori
        self.callback = callback

        self.nome.setText(self.controller.get_nome_allenatore())
        self.cognome.setText(self.controller.get_cognome_allenatore())
        self.codiceFiscale.setText(self.controller.get_codfis_allenatore())
        self.id.setText(self.controller.get_id_allenatore())
        self.dataDiNascita.setText(self.controller.get_dataNascita_allenatore().strftime("%d/%m/%Y"))
        self.eta.setText(self.controller.get_eta_allenatore())
        self.telefono.setText(self.controller.get_telefono_allenatore())
        self.email.setText(self.controller.get_email_allenatore())
        self.licenza.setText(self.controller.get_licenza_allenatore())
        self.button_conferma.hide()

        self.button_elimina.clicked.connect(self.elimina_allenatore)
        self.button_modifica.clicked.connect(self.modifica_allenatore)
        self.button_conferma.clicked.connect(self.conferma_modifica)

    def elimina_allenatore(self):
        self.elimina_callback(self.controller.get_id_allenatore())
        self.controllerAllenatori.save_data()
        self.controllerUtenti.rimuovi_utente_by_id(self.controller.get_id_allenatore())
        self.controllerUtenti.save_data()
        delete(self.controller.get_id_allenatore())
        self.callback()
        self.close()

    def modifica_allenatore(self):
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

        self.controller.set_nome_allenatore(self.nome.text())
        self.controller.set_cognome_allenatore(self.cognome.text())
        self.controller.set_codfis_allenatore(self.codiceFiscale.text())
        self.controller.set_dataNascita_allenatore(self.dataDiNascita.text())
        self.controller.set_eta_allenatore(self.eta.text())
        self.controller.set_telefono_allenatore(self.telefono.text())
        self.controller.set_email_allenatore(self.email.text())
        self.controller.set_licenza_allenatore(self.licenza.text())
        self.controllerUtenti.save_data()

        # recuperare bene elemento dalla lista clienti (sbagliato)

        allenatore_allenatori = self.controllerAllenatori.get_allenatore_by_id(self.controller.get_id_allenatore())
        controllerAllenatore_allenatori = ControlloreAllenatore(allenatore_allenatori)
        controllerAllenatore_allenatori.set_nome_allenatore(self.nome.text())
        controllerAllenatore_allenatori.set_cognome_allenatore(self.cognome.text())
        controllerAllenatore_allenatori.set_codfis_allenatore(self.codiceFiscale.text())
        controllerAllenatore_allenatori.set_dataNascita_allenatore(self.dataDiNascita.text())
        controllerAllenatore_allenatori.set_eta_allenatore(self.eta.text())
        controllerAllenatore_allenatori.set_telefono_allenatore(self.telefono.text())
        controllerAllenatore_allenatori.set_email_allenatore(self.email.text())
        controllerAllenatore_allenatori.set_licenza_allenatore(self.licenza.text())
        self.controllerAllenatori.save_data()
        self.callback()





from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from servizi.controller.ControlloreCorso import ControlloreCorso
from servizi.view.corso.view.vistainserimentoiscritto.VistaInserimentoIscritto import VistaInserimentoIscritto


class VistaCorso(QWidget):
    def __init__(self, corso, callback, salvataggio, parent=None):
        super(VistaCorso, self).__init__(parent)
        uic.loadUi('servizi/view/corso/view/vistacorso/vistaVisualizzaIscrittiCorso.ui', self)
        self.controller = ControlloreCorso(corso)
        self.callback = callback
        self.salvataggio = salvataggio

        controllerLista = ControllerListaClienti()
        self.listaConRipetizioni = controllerLista.get_lista_clienti()
        self.iscrivibili = []

        self.update_ui()
        self.tipo.setText(self.controller.get_tipo_corso())

        self.button_inserisciIscritti.clicked.connect(self.add_iscritto)
        self.button_rimuoviIscritti.clicked.connect(self.elimina_iscritto)


    def add_iscritto(self):
        if self.controller.verifica_iscritti_corso():
            self.filtraLista()
            if len(self.iscrivibili) != 0:
                self.vistaInserimento = VistaInserimentoIscritto(self.controller, self.iscrivibili, self.update_ui)
                self.vistaInserimento.show()
            else:
                QMessageBox.critical(self, 'Errore', 'Non ci sono clienti da aggiungere', QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(self, 'Errore', 'Numero massimo di iscritti raggiunti', QMessageBox.StandardButton.Ok)

    def elimina_iscritto(self):
        selected = self.list_view.selectedIndexes()[0].row()
        iscritto_selezionato = self.controller.get_lista_iscritti_corso()[selected]
        self.controller.elimina_iscritto_corso_by_id(iscritto_selezionato.id)
        self.update_ui()
        self.salvataggio()


    def update_ui(self):
        self.numeroIscritti.setText(str(self.controller.get_num_iscritti_corso()))
        if(self.controller.get_num_iscritti_corso() == 0):
            self.button_rimuoviIscritti.hide()
        else:
            self.button_rimuoviIscritti.show()
        self.listview_model = QStandardItemModel(self.list_view)
        for iscritto in self.controller.get_lista_iscritti_corso():
            item = QStandardItem()
            item.setText(f"{iscritto.cognome} {iscritto.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def filtraLista(self):
        for cl in self.listaConRipetizioni:
            contrCl = ControlloreCliente(cl)
            if contrCl.get_abbonato_cliente():
                f = 0
                for iscr in self.controller.get_lista_iscritti_corso():
                    if cl.id == iscr.id:
                        f = 1
                        break
                if f == 0:
                    self.iscrivibili.append(cl)


    def closeEvent(self, event):
        self.callback()
        self.salvataggio()




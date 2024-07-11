from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti


class VistaInserimentoIscritto(QWidget):
    def __init__(self, controller, iscrivibili, callback, parent=None):
        super(VistaInserimentoIscritto, self).__init__(parent)
        uic.loadUi('servizi/view/corso/view/vistainserimentoiscritto/vistaInserisciNuovoIscritto.ui', self)
        self.controller = controller
        self.callback = callback
        self.iscrivibili = iscrivibili
        #print(len(self.iscrivibili))
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.iscrivibili:
            item = QStandardItem()
            item.setText(f"{cliente.cognome} {cliente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

        self.button_conferma.clicked.connect(self.inserisciIscritto)

    def inserisciIscritto(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.cliente_selezionato = self.iscrivibili[selected]  # self.controllerLista.get_cliente_by_index(selected)
        self.controller.aggiungi_iscritto_corso(self.cliente_selezionato)
        self.callback()
        self.iscrivibili.clear()
        self.close()

    def closeEvent(self, event):
        self.iscrivibili.clear()
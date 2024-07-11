from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from servizi.controller.ControlloreCorso import ControlloreCorso
from servizi.view.corso.view.VistaInserisciCorso import VistaInserisciCorso
from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi


class VistaListaCorsi(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaCorsi, self).__init__(parent)

        uic.loadUi('listacorsi/view/vistaGestisciCorsi.ui', self)
        self.controller = ControlloreListaCorsi()
        self.home = home

        self.update_ui()

        self.button_inserisciCorso.clicked.connect(self.show_new_corso)
        self.button_eliminaCorso.clicked.connect(self.delete_selected)



    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for corso in self.controller.get_lista_corsi():
            item = QStandardItem()
            item.setText(f"{corso.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

    def delete_selected(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.corso_selezionato = self.controller.get_corso_by_index(selected)
        controller_corso_selezionato = ControlloreCorso(self.corso_selezionato)
        self.controller.rimuovi_corso_by_id(controller_corso_selezionato.get_id_corso())
        self.update_ui()
        self.controller.save_data()

    def show_new_corso(self):
        self.vista_inserisci_corso = VistaInserisciCorso(self.controller, self.update_ui, self.controller.save_data)
        self.vista_inserisci_corso.show()

from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi
from servizi.view.corso.view.vistacorso.VistaCorso import VistaCorso


class VistaListaCorsiAllenatore(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaCorsiAllenatore, self).__init__(parent)

        uic.loadUi('listacorsi/view/gestionecorsiallenatore/view/vistaIscrittiCorso.ui', self)
        self.controller = ControlloreListaCorsi()
        self.home = home

        self.update_ui()

        self.button_visualizzaCorso.clicked.connect(self.show_selected_info)


    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for corso in self.controller.get_lista_corsi():
            item = QStandardItem()
            item.setText(f"{corso.tipo} {corso.numIscritti}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.corso_selezionato = self.controller.get_corso_by_index(selected)
        self.vista_corso = VistaCorso(self.corso_selezionato, self.update_ui, self.controller.save_data)
        self.vista_corso.show()

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from attivita.controller.ControlloreRicevuta import ControlloreRicevuta
from attivita.view.ricevuta.VistaInserisciRicevuta import VistaInserisciRicevuta
from listaricevute.controller.ControlloreListaRicevute import ControlloreListaRicevute


class VistaListaRicevute(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaRicevute, self).__init__(parent)
        uic.loadUi('listaricevute/view/vistaGestisciRicevute.ui', self)

        self.controller = ControlloreListaRicevute()
        self.home = home

        self.update_ui()

        self.button_inserisci.clicked.connect(self.show_new_ricevuta)
        self.button_elimina.clicked.connect(self.delete_selected)



    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for ricevuta in self.controller.get_lista_ricevute():
            data = ricevuta.data.strftime("%d/%m/%Y")
            item = QStandardItem()
            item.setText(f"{ricevuta.codiceFiscale} {data} {ricevuta.prezzo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def show_new_ricevuta(self):
        self.vista_inserisci_ricevuta = VistaInserisciRicevuta(self.controller, self.update_ui, self.controller.save_data)
        self.vista_inserisci_ricevuta.show()


    def delete_selected(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.ricevuta_selezionata = self.controller.get_ricevuta_by_index(selected)
        controller_ricevuta_selezionata = ControlloreRicevuta(self.ricevuta_selezionata)
        self.controller.rimuovi_ricevuta_by_id(controller_ricevuta_selezionata.get_id_ricevuta())
        self.update_ui()
        self.controller.save_data()

    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

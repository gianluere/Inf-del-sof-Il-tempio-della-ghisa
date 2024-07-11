from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from servizi.controller.ControlloreVisita import ControlloreVisita
from servizi.view.visita.view.vistainseriscivisita.VistaInserisciVisita import VistaInserisciVisita
from listavisite.controller.ControlloreListaVisite import ControlloreListaVisite


class VistaListaVisite(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaVisite, self).__init__(parent)

        uic.loadUi('listavisite/view/GestioneVisite.ui', self)
        self.controller = ControlloreListaVisite()
        self.home = home

        self.update_ui()

        self.button_inserisciVisita.clicked.connect(self.show_new_corso)
        self.button_eliminaVisita.clicked.connect(self.delete_selected)


    #L'errore per il quale crasha è in update_ui
    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)
        for visita in self.controller.get_lista_visite():
            item = QStandardItem()
            item.setText(f"{visita.id} {visita.codiceFiscale} {visita.data} {visita.ora}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

    def delete_selected(self):
        selected = self.listView.selectedIndexes()[0].row()
        self.visita_selezionata = self.controller.get_visita_by_index(selected)
        controller_visita_selezionata = ControlloreVisita(self.visita_selezionata)
        self.controller.rimuovi_visita_by_id(controller_visita_selezionata.get_id_visita())
        self.update_ui()
        self.controller.save_data()

    def show_new_corso(self):
        self.vista_inserisci_visita = VistaInserisciVisita(self.controller, self.update_ui, self.controller.save_data)
        self.vista_inserisci_visita.show()


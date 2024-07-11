from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from Utilizzatore.view.cliente.vistaCliente2.VistaVisualizzaCliente2 import VistaVisualizzaCliente2
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listadiete.controller.ControlloreListaDiete import ControlloreListaDiete
from listaschede.controller.ControlloreListaSchede import ControlloreListaSchede
from servizi.controller.ControlloreDieta import ControlloreDieta
from servizi.controller.ControlloreScheda import ControlloreScheda


class VistaListaClienti(QWidget):
    def __init__(self, home, filtro, parent=None):
        super(VistaListaClienti, self).__init__(parent)

        uic.loadUi('listaclienti/view/VisualizzaListaCliente.ui', self)
        self.controller = ControllerListaClienti()
        self.lista_filtrata = []

        if filtro == "allenatore":
            controllore_schede = ControlloreListaSchede()
            controllore_clienti = ControllerListaClienti()

            for sc in controllore_schede.get_lista_schede():
                for cl in controllore_clienti.get_lista_clienti():
                    if ControlloreScheda(sc).get_id_scheda() == ControlloreCliente(cl).get_id_cliente():
                        self.lista_filtrata.append(cl)
        else:
            controllore_diete = ControlloreListaDiete()
            controllore_clienti = ControllerListaClienti()

            for die in controllore_diete.get_lista_diete():
                for cl in controllore_clienti.get_lista_clienti():
                    if ControlloreDieta(die).get_id_dieta() == ControlloreCliente(cl).get_id_cliente():
                        self.lista_filtrata.append(cl)

        self.home = home
        self.update_ui()
        self.button_ottieniInformazioni.clicked.connect(self.show_selected_info)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for cliente in self.lista_filtrata:
            item = QStandardItem()
            item.setText(f"{cliente.cognome} {cliente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)


    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.cliente_selezionato = self.lista_filtrata[selected]

        self.vista_cliente = VistaVisualizzaCliente2(self.cliente_selezionato)
        self.vista_cliente.show()

    def closeEvent(self, event):
        self.home.show()

from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem


from Utilizzatore.view.allenatore.VistaInserisciAllenatore import VistaInserisciAllenatore
from Utilizzatore.view.allenatore.vistaAllenatore.VistaVisualizzaAllenatore import VistaVisualizzaAllenatore
from Utilizzatore.view.cliente.VistaInserisciCliente import VistaInserisciCliente
from Utilizzatore.view.cliente.vistaCliente.VistaVisualizzaCliente import VistaVisualizzaCliente
from Utilizzatore.view.nutrizionista.VistaInserisciNutrizionista import VistaInserisciNutrizionista
from Utilizzatore.view.nutrizionista.vistaNutrizionista.VistaVisualizzaNutrizionista import VistaVisualizzaNutrizionista
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listanutrizionisti.controller.ControlloreListaNutrizionisti import ControllerListaNutrizionisti
from listautenti.controller.ControlloreListaUtenti import ControllerListaUtenti
from listaallenatori.controller.ControlloreListaAllenatori import ControllerListaAllenatori


class VistaListaUtenti(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaUtenti, self).__init__(parent)

        uic.loadUi('listautenti/view/vistaListaUtenti.ui', self)
        self.controller = ControllerListaUtenti()
        self.controllerClienti = ControllerListaClienti()
        self.controllerAllenatori = ControllerListaAllenatori()
        self.controllerNutrizionisti = ControllerListaNutrizionisti()
        self.home = home

        self.update_ui()

        self.ins_cliente_button.clicked.connect(self.show_new_cliente)
        self.ins_all_button.clicked.connect(self.show_new_allenatore)
        self.ins_nutr_button.clicked.connect(self.show_new_nutrizionista)
        self.button_informazioni.clicked.connect(self.show_selected_info)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for utente in self.controller.get_lista_utenti():
            item = QStandardItem()
            item.setText(f"{utente.id} {utente.cognome} {utente.nome}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

    def show_new_cliente(self):
        self.vista_inserisci_cliente = VistaInserisciCliente(self.controller, self.update_ui, self.controllerClienti,
                                                             self.controllerClienti.save_data)
        self.vista_inserisci_cliente.show()

    def show_new_allenatore(self):
        self.vista_inserisci_allenatore = VistaInserisciAllenatore(self.controller, self.update_ui,
                                                                   self.controllerAllenatori,
                                                                   self.controllerAllenatori.save_data)
        self.vista_inserisci_allenatore.show()

    def show_new_nutrizionista(self):
        self.vista_inserisci_nutrizionista = VistaInserisciNutrizionista(self.controller, self.update_ui,
                                                                         self.controllerNutrizionisti,
                                                                         self.controllerNutrizionisti.save_data)
        self.vista_inserisci_nutrizionista.show()

    def show_selected_info(self):
        selected = self.list_view.selectedIndexes()[0].row()
        self.utente_selezionato = self.controller.get_utente_by_index(selected)
        if type(self.utente_selezionato).__name__ == "Cliente":
            self.vista_cliente = VistaVisualizzaCliente(self.utente_selezionato, self.controllerClienti.rimuovi_cliente_by_id, self.controller, self.controllerClienti, self.update_ui)
            self.vista_cliente.show()
        elif type(self.utente_selezionato).__name__ == "Nutrizionista":
            self.vista_nutrizionista = VistaVisualizzaNutrizionista(self.utente_selezionato,
                                                        self.controllerNutrizionisti.rimuovi_nutrizionista_by_id, self.controller,
                                                        self.controllerNutrizionisti, self.update_ui)
            self.vista_nutrizionista.show()
        elif type(self.utente_selezionato).__name__ == "Allenatore":
            self.vista_allenatore = VistaVisualizzaAllenatore(self.utente_selezionato,
                                                        self.controllerAllenatori.rimuovi_allenatore_by_id, self.controller,
                                                        self.controllerAllenatori, self.update_ui)
            self.vista_allenatore.show()


from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from servizi.controller.ControlloreIngresso import ControlloreIngresso
from servizi.view.ingresso.VistaInserisciIngresso import VistaInserisciIngresso
from listaingressi.controller.ControlloreListaIngressi import ControlloreListaIngressi

class VistaListaIngressi(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaIngressi, self).__init__(parent)
        uic.loadUi('listaingressi/view/vistaGestisciIngressi.ui', self)
        self.controller = ControlloreListaIngressi()
        self.home = home

        self.update_ui()

        self.button_inserisciIngresso.clicked.connect(self.show_new_ingresso)
        #self.button_eliminaCorso.clicked.connect(self.delete_selected)



    def update_ui(self):
        self.ingressiConAbbonamento.setText(str(self.controller.get_numero_con_abbonamento()))
        self.ingressiSenzaAbbonamento.setText(str(self.controller.get_numero_senza_abbonamento()))




    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

    #def delete_selected(self):
     #   selected = self.list_view.selectedIndexes()[0].row()
      #  self.corso_selezionato = self.controller.get_corso_by_index(selected)
       # controller_corso_selezionato = ControlloreCorso(self.corso_selezionato)
        #self.controller.rimuovi_corso_by_id(controller_corso_selezionato.get_id_corso())
        #self.update_ui()
        #self.controller.save_data()

    def show_new_ingresso(self):
        self.vista_inserisci_ingresso = VistaInserisciIngresso(self, self.controller, self.update_ui, self.controller.save_data)
        self.hide()
        self.vista_inserisci_ingresso.show()

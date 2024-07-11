from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from servizi.controller.ControlloreAgenda import ControlloreAgenda
from servizi.model.Agenda import Agenda

class VistaVisualizzaAgenda(QWidget):

    def __init__(self, home, controller_cl):
        super(VistaVisualizzaAgenda,self).__init__()
        uic.loadUi("servizi/view/agenda/VisualizzaAgenda.ui", self)
        self.home = home
        self.controller_cl = controller_cl
        self.controller = ControlloreAgenda(Agenda(self.controller_cl.get_id_cliente()))
        self.update_ui()


    def update_ui(self):
        self.listview_model = QStandardItemModel(self.listView)
        for corso in self.controller.get_lista_corsi_cliente():
            item = QStandardItem()
            item.setText(f"{corso.tipo}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.listView.setModel(self.listview_model)

        self.listview_model_2 = QStandardItemModel(self.listView_2)
        for visita in self.controller.get_lista_visite_cliente():
            item2 = QStandardItem()
            item2.setText(f"{visita.data}  {visita.ora}")
            item2.setEditable(False)
            font2 = item2.font()
            font2.setPointSize(18)
            item2.setFont(font2)
            self.listview_model_2.appendRow(item2)
        self.listView_2.setModel(self.listview_model_2)

    def closeEvent(self, event):
        self.close()
        self.home.show()

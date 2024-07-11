from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox
from datetime import date
from datetime import datetime, timedelta

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from listaabbonamenti.controller.ControlloreListaAbbonamenti import ControlloreListaAbbonamenti
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi
from listautenti.controller.ControlloreListaUtenti import ControllerListaUtenti
from servizi.controller.ControlloreAbbonamento import ControlloreAbbonamento
from servizi.controller.ControlloreAgenda import ControlloreAgenda
from servizi.controller.ControlloreCorso import ControlloreCorso
from servizi.model.Agenda import Agenda
from servizi.view.abbonamento.VistaInserisciAbbonamento import VistaInserisciAbbonamento


class VistaListaAbbonamenti(QWidget):
    def __init__(self, home, parent=None):
        super(VistaListaAbbonamenti, self).__init__(parent)

        uic.loadUi('listaabbonamenti/view/vistaGestisciAbbonamenti.ui', self)
        self.controller = ControlloreListaAbbonamenti()
        self.home = home
        self.update_ui()

        self.button_inserisci.clicked.connect(self.show_new_abbonamento)
        self.button_elimina.clicked.connect(self.delete_selected)
        self.button_sospendi.clicked.connect(self.sospendi_selected)
        self.button_attiva.clicked.connect(self.attiva_abbonamento)

    def update_ui(self):
        self.listview_model = QStandardItemModel(self.list_view)
        for abb in self.controller.get_lista_abbonamenti():
            dataIn = abb.dataInizio.strftime("%d/%m/%Y")
            dataSc = abb.dataScadenza.strftime("%d/%m/%Y")
            item = QStandardItem()
            if abb.dataSospensione is None:
                item.setText(f"{abb.id} {dataIn} {dataSc}")
            else:
                dataSos = abb.dataSospensione.strftime("%d/%m/%Y")
                item.setText(f"{abb.id} {dataIn} {dataSc} Data sospensione: {dataSos}")
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.list_view.setModel(self.listview_model)

    def show_new_abbonamento(self):
        self.vistaInserimento = VistaInserisciAbbonamento(self.controller, self.update_ui, self.controller.save_data)
        self.vistaInserimento.show()


    def delete_selected(self):
        controlloreAbb = ControlloreAbbonamento(self.controller.get_abbonamento_by_index(self.list_view.selectedIndexes()[0].row()))

        controlloreClienti = ControllerListaClienti()
        controCliente = ControlloreCliente(controlloreClienti.get_cliente_by_id(controlloreAbb.get_id_abbonamento()))
        controCliente.set_abbonamento_cliente(None)
        controCliente.set_abbonato_cliente(False)
        controlloreClienti.save_data()
        controlloreUtenti = ControllerListaUtenti()
        clienteUtenti = ControlloreCliente(controlloreUtenti.get_utente_by_id(controlloreAbb.get_id_abbonamento()))
        clienteUtenti.set_abbonamento_cliente(None)
        clienteUtenti.set_abbonato_cliente(False)
        controlloreUtenti.save_data()

        lista_corsi_cl = ControlloreAgenda(Agenda(controlloreAbb.get_id_abbonamento())).get_lista_corsi_cliente()
        controlloreListaCorsi = ControlloreListaCorsi()

        for corso_cl in lista_corsi_cl:
            for corso in controlloreListaCorsi.get_lista_corsi():
                controlloreCorso = ControlloreCorso(corso)
                if controlloreCorso.get_id_corso() == ControlloreCorso(corso_cl).get_id_corso():
                    controlloreCorso.elimina_iscritto_corso_by_id(controCliente.get_id_cliente())
        controlloreListaCorsi.save_data()

        self.controller.rimuovi_abbonamento_by_id(controlloreAbb.get_id_abbonamento())
        self.controller.save_data()
        self.update_ui()


    def sospendi_selected(self):
        controlloreAbb = ControlloreAbbonamento(self.controller.get_abbonamento_by_index(self.list_view.selectedIndexes()[0].row()))
        if controlloreAbb.get_tipologia_abbonamento() == "Annuale":
            controlloreAbb.set_data_sospensione(datetime.now().strftime("%d/%m/%Y"))

            controlloreClienti = ControllerListaClienti()
            controCliente = ControlloreCliente(controlloreClienti.get_cliente_by_id(controlloreAbb.get_id_abbonamento()))
            controCliente.set_abbonato_cliente(False)
            controlloreClienti.save_data()
            controlloreUtenti = ControllerListaUtenti()
            clienteUtenti = ControlloreCliente(controlloreUtenti.get_utente_by_id(controlloreAbb.get_id_abbonamento()))
            clienteUtenti.set_abbonato_cliente(False)
            controlloreUtenti.save_data()

            lista_corsi_cl = ControlloreAgenda(Agenda(controlloreAbb.get_id_abbonamento())).get_lista_corsi_cliente()
            controlloreListaCorsi = ControlloreListaCorsi()

            for corso_cl in lista_corsi_cl:
                for corso in controlloreListaCorsi.get_lista_corsi():
                    controlloreCorso = ControlloreCorso(corso)
                    if controlloreCorso.get_id_corso() == ControlloreCorso(corso_cl).get_id_corso():
                        controlloreCorso.elimina_iscritto_corso_by_id(controCliente.get_id_cliente())
            controlloreListaCorsi.save_data()
            self.controller.save_data()
            self.update_ui()
        else:
            QMessageBox.warning(self, 'Attenzione', 'È possibile sospendere solo gli abbonamenti annuali',
                                QMessageBox.StandardButton.Ok)


    def attiva_abbonamento(self):
        controlloreAbb = ControlloreAbbonamento(self.controller.get_abbonamento_by_index(self.list_view.selectedIndexes()[0].row()))
        if controlloreAbb.get_data_sospensione() is None:
            QMessageBox.warning(self, 'Attenzione', "L'abbonamento è già attivo",
                                QMessageBox.StandardButton.Ok)
        else:
            differenza = datetime.now().date() - controlloreAbb.get_data_sospensione()
            print(differenza, " ", differenza.days)
            nuova_scadenza = controlloreAbb.get_data_scadenza() + timedelta(days=differenza.days)
            print(nuova_scadenza)
            nuova_scadenza_formattata = nuova_scadenza.strftime('%d/%m/%Y')
            controlloreAbb.set_data_scadenza(nuova_scadenza_formattata)
            controlloreAbb.set_data_sospensione(None)

            controlloreClienti = ControllerListaClienti()
            controCliente = ControlloreCliente(controlloreClienti.get_cliente_by_id(controlloreAbb.get_id_abbonamento()))
            controCliente.set_abbonato_cliente(True)
            controCliente.set_abbonamento_cliente(controlloreAbb.model)
            controlloreClienti.save_data()
            controlloreUtenti = ControllerListaUtenti()
            clienteUtenti = ControlloreCliente(controlloreUtenti.get_utente_by_id(controlloreAbb.get_id_abbonamento()))
            clienteUtenti.set_abbonato_cliente(True)
            clienteUtenti.set_abbonamento_cliente(controlloreAbb.model)
            controlloreUtenti.save_data()
            self.controller.save_data()
            self.update_ui()


    def closeEvent(self, event):
        self.controller.save_data()
        self.home.show()

from PyQt6.QtGui import QStandardItem

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from Utilizzatore.model.Cliente import Cliente
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi
from listavisite.controller.ControlloreListaVisite import ControlloreListaVisite
from servizi.controller import ControlloreAgenda
from servizi.controller.ControlloreCorso import ControlloreCorso
from servizi.model.Servizio import Servizio

class Agenda(Servizio):

    def __init__(self, id):
        super(Agenda, self).__init__(id) #id uguale al cliente


    def get_lista_corsi_cliente(self):
        lista_corsi_cliente = []
        controller_corsi = ControlloreListaCorsi()
        for corso in controller_corsi.get_lista_corsi():
            controller_corso = ControlloreCorso(corso)
            lista_iscr = controller_corso.get_lista_iscritti_corso()
            for iscritto in lista_iscr:
                if self.id == iscritto.id:
                    lista_corsi_cliente.append(corso)
                    break
        return lista_corsi_cliente

    def get_lista_visite_cliente(self):
        lista_visite_cliente = []
        controllore_cliente = ControlloreCliente(ControllerListaClienti().get_cliente_by_id(self.id))
        controller_visite = ControlloreListaVisite()
        for visita in controller_visite.get_lista_visite():
            if controllore_cliente.get_codfis_cliente() == visita.codiceFiscale:
                lista_visite_cliente.append(visita)
        return lista_visite_cliente







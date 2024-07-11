from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listaingressi.controller.ControlloreListaIngressi import ControlloreListaIngressi


class GestoreStatistiche():
    def __init__(self):
        self.numero_clienti = [
            self.calcola_numero_clienti_nel_range(0, 16),
            self.calcola_numero_clienti_nel_range(17, 24),
            self.calcola_numero_clienti_nel_range(25, 35),
            self.calcola_numero_clienti_nel_range(36, 45),
            self.calcola_numero_clienti_nel_range(46, 99)
        ]
        controller = ControlloreListaIngressi()
        self.ingressi = [
            controller.get_numero_con_abbonamento(),
            controller.get_numero_senza_abbonamento()
        ]
        self.fasce_eta = ['0-16', '17-24', '25-35', '36-45', '46-99']

    def calcola_numero_clienti_nel_range(self, min, max):
        controller = ControllerListaClienti()
        clienti = 0
        for cliente in controller.get_lista_clienti():
            controller_cl = ControlloreCliente(cliente)
            if min <= int(controller_cl.get_eta_cliente()) <= max:
                clienti += 1

        return clienti

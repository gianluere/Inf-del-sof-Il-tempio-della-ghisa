import os
import time
import schedule
from datetime import datetime

from Utilizzatore.controller.ControlloreCliente import ControlloreCliente
from attivita.model.Avviso import Avviso
from listaabbonamenti.controller.ControlloreListaAbbonamenti import ControlloreListaAbbonamenti

from listaclienti.controller.ControlloreListaClienti import ControllerListaClienti
from listacorsi.controller.ControlloreListaCorsi import ControlloreListaCorsi
from listautenti.controller.ControlloreListaUtenti import ControllerListaUtenti
from servizi.controller.ControlloreAbbonamento import ControlloreAbbonamento
from servizi.controller.ControlloreAgenda import ControlloreAgenda
from servizi.controller.ControlloreCorso import ControlloreCorso
from servizi.model.Agenda import Agenda

os.chdir(os.path.dirname('../'))
#print(os.getcwd())

def controlla_scaduti():
    controller_lista_abbonamenti = ControlloreListaAbbonamenti()
    #print(len(controller_lista_abbonamenti.get_lista_abbonamenti()))
    abbonamenti = controller_lista_abbonamenti.get_lista_abbonamenti()

    for abb in abbonamenti[:]: #in questo modo non modifico la lista che sto scorrendo
        controller_abb = ControlloreAbbonamento(abb)
        if controller_abb.get_data_scadenza() < datetime.now().date() and controller_abb.get_data_sospensione() is None:
            controlloreClienti = ControllerListaClienti()
            controCliente = ControlloreCliente(controlloreClienti.get_cliente_by_id(controller_abb.get_id_abbonamento()))
            controCliente.set_abbonamento_cliente(None)
            controCliente.set_abbonato_cliente(False)
            controlloreClienti.save_data()
            controlloreUtenti = ControllerListaUtenti()
            clienteUtenti = ControlloreCliente(controlloreUtenti.get_utente_by_id(controller_abb.get_id_abbonamento()))
            clienteUtenti.set_abbonamento_cliente(None)
            clienteUtenti.set_abbonato_cliente(False)
            controlloreUtenti.save_data()

            lista_corsi_cl = ControlloreAgenda(Agenda(controller_abb.get_id_abbonamento())).get_lista_corsi_cliente()
            controlloreListaCorsi = ControlloreListaCorsi()

            for corso_cl in lista_corsi_cl:
                for corso in controlloreListaCorsi.get_lista_corsi():
                    controllerCorso = ControlloreCorso(corso)
                    if controllerCorso.get_id_corso() == ControlloreCorso(corso_cl).get_id_corso():
                        controllerCorso.elimina_iscritto_corso_by_id(controCliente.get_id_cliente())
            controlloreListaCorsi.save_data()
            controller_lista_abbonamenti.rimuovi_abbonamento_by_id(controller_abb.get_id_abbonamento())
            controller_lista_abbonamenti.save_data()
            avv = Avviso(controCliente.get_email_cliente(), 'Scandenza abbonamento', 'Salve, la informiamo che il suo abbonamento è scaduto')
            avv.send_avviso()


controlla_scaduti()
schedule.every().day.at("02:00").do(controlla_scaduti)


while True:
    schedule.run_pending()
    time.sleep(1)

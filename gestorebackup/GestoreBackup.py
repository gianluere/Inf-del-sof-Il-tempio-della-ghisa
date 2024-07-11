import os
import shutil
import time
import schedule

# Directory dell'applicazione e directory di destinazione
destination_directory = os.path.join(os.path.expanduser('~'), 'Desktop/Backup')
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)


def download_pickle_files():
    pickle_files = [
        os.path.abspath('../listaingressi/data/lista_ingressi_salvata.pickle'),
        os.path.abspath('../listaabbonamenti/data/lista_abbonamenti_salvata.pickle'),
        os.path.abspath('../listaallenatori/data/lista_allenatori_salvata.pickle'),
        os.path.abspath('../listaclienti/data/lista_clienti_salvata.pickle'),
        os.path.abspath('../listacorsi/data/lista_corsi_salvata.pickle'),
        os.path.abspath('../listadiete/data/lista_diete_salvata.pickle'),
        os.path.abspath('../listanutrizionisti/data/lista_nutrizionisti_salvata.pickle'),
        os.path.abspath('../listaricevute/data/lista_ricevute_salvata.pickle'),
        os.path.abspath('../listaschede/data/lista_schede_salvata.pickle'),
        os.path.abspath('../listautenti/data/lista_utenti_salvata.pickle'),
        os.path.abspath('../listavisite/data/lista_visite_salvata.pickle')
    ]

    for file_path in pickle_files:
        if os.path.exists(file_path):
            shutil.copy(file_path, destination_directory)
            #print(f'File {file_path} copiato in {destination_directory}')


#schedule.every(2).hours.do(download_pickle_files)
#schedule.every(1).minutes.do(download_pickle_files)
schedule.every().day.at("02:00").do(download_pickle_files)
download_pickle_files()

# Loop infinito per eseguire il lavoro ogni 2 ore
while True:
    schedule.run_pending()
    time.sleep(1)

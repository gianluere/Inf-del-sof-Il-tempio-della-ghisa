import os
import sys
import subprocess
from PyQt6.QtWidgets import QApplication

from login.view.VistaLogin import VistaLogin


if __name__ == '__main__':


    server_path = os.path.abspath('login/model/Server.py')
    server_working_directory = os.path.dirname(server_path)
    server = subprocess.Popen([sys.executable, server_path], cwd=server_working_directory)
    #print(server.pid)


    backup_path = os.path.abspath('gestorebackup/GestoreBackup.py')
    # Directory di lavoro del sottoprocesso
    working_directory = os.path.dirname(backup_path)
    backup = subprocess.Popen(
        [sys.executable, backup_path],
        cwd=working_directory  # Imposta la directory di lavoro del sottoprocesso
    )
    #print(backup.pid)

    avvisi_path = os.path.abspath('gestoreavvisi/GestoreAvvisi.py')
    avvisi_working_directory = os.path.dirname(avvisi_path)
    avvisi = subprocess.Popen([sys.executable, avvisi_path], cwd=avvisi_working_directory)
    #print(avvisi.pid)

    app = QApplication(sys.argv)
    vistahome = VistaLogin(backup, server, avvisi)
    vistahome.show()
    sys.exit(app.exec())


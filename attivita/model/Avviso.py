import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Avviso:
    def __init__(self, to, subject, body):
        self.to = to.split(", ")
        self.subject = subject
        self.body = body

    def send_avviso(self):
        # Parametri del server SMTP di Gmail
        smtp_server = 'smtp.gmail.com'
        porta = 587  # Porta SMTP per Gmail
        username = 'ingdelsof@gmail.com'
        password = 'iqfznsbzdcjauxwh'

        # Destinatario e corpo del messaggio
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = ', '.join(self.to)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        # Connessione al server SMTP di Gmail
        server = smtplib.SMTP(smtp_server, porta)
        server.ehlo()
        server.starttls()  # Avvia la crittografia TLS
        server.login(username, password)
        server.sendmail(username, self.to, msg.as_string())

        # Chiusura della connessione SMTP
        server.quit()

# IMPORTANTE LEGGERE TUTTO IL README

Per il corretto funzionamento del programma, ogni volta il programma DEVE essere chiuso dalla finestra di login
(esempio: ci troviamo nella home amministratore, per chiuderlo dobbiamo fare prima il logout e dopo chiudere la finestra del login)

Nel caso si abbia un mac, potrebbe succedere che in caso di chiusura non corretta del programma, il sottoprocesso del server non venga chiuso e di conseguenza la porta socket 60001 resti occupata. In quel caso bisogna chiudere il sottoprocesso con il PID che sta operando su quella porta

## macOS:
```
lsof -i :63001 -> comando per trovare il nome del PID che opera su quella porta
kill -9 numeropid -> comando per killare il processo con il PID immesso
```

## Windows:
```
netstat -aon | findstr :63001 -> comando per trovare il nome del PID che opera su quella porta
taskkill /PID [PID] /F -> (sostituire [PID] con il PID effettivo del processo) comando per killare il processo con il PID immesso
```

## Credenziali per GMAIL
Le credenziali per accedere a GMAIL sono:
  Email: ingdelsof@gmail.com
  Password: ingdelsof@123
Purtroppo non è possibile accedervi poiché è abilitata l'autenticazione a due fattori, il giorno della presentazione del progetto faremo una dimostrazione del funzionamento

## Utenti attualmente presenti nel database:
| User   | Password    | TipoUtente    |
| ------ | ----------- | ------------- |
| amm    | amm         | Amministratore|
| gian   | eremita     | Cliente       |
| stef   | calandrella | Cliente       |
| sim    | sticca      | Allenatore    |
| ettore | ericci      | Nutrizionista |

## Per il backup:
All'avvio del main, verrà creata una cartella chiamata Backup sul desktop (nel caso in cui non sia presente) e verrà fatta la copia dei file. Poi procederà con gli orari prestabiliti.

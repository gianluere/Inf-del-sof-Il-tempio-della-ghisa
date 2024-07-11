Per il corretto funzionamento del programma, ogni volta il programma DEVE essere chiuso dalla finestra di login
(esempio: ci troviamo nella home amministratore, per chiuderlo dobbiamo fare prima il logout e dopo chiudere la finestra del login)

Nel caso si abbia un mac, potrebbe succedere che in caso di chiusura non corretta del programma, il sottoprocesso del server non venga chiuso e di conseguenza la porta socket 60001 resti occupata. In quel caso bisogna chiudere il sottroprocesso con il PID che sta operando su quella porta

lsof -i :63001 -> comando per trovare il nome del PID che opera su quella porta
kill -9 numeropid -> comando per killare il processo con il PID immesso

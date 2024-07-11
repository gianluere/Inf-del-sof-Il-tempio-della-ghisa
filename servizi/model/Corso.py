from servizi.model.Servizio import Servizio


class Corso(Servizio):
    def __init__(self, id, tipo):
        super(Corso, self).__init__(id)
        self.tipo = tipo
        self.listaIscritti = []
        self.numIscritti = 0

    def aggiungi_iscritto_corso(self, iscritto):
        self.listaIscritti.append(iscritto)
        self.numIscritti += 1

    def verifica_iscritti_corso(self):
        return self.numIscritti < 50

    def get_lista_iscritti_corso(self):
        return self.listaIscritti

    def elimina_iscritto_corso_by_id(self, id):
        def is_selected(iscr):
            if iscr.id == id:
                return True
            return False

        self.listaIscritti.remove(list(filter(is_selected, self.listaIscritti))[0])
        self.numIscritti -= 1

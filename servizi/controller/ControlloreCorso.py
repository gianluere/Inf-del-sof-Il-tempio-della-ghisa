class ControlloreCorso():
    def __init__(self, corso):
        self.model = corso

    def get_id_corso(self):
        return self.model.id

    def get_tipo_corso(self):
        return self.model.tipo

    def get_lista_iscritti_corso(self):
        return self.model.get_lista_iscritti_corso()

    def get_num_iscritti_corso(self):
        return self.model.numIscritti

    def verifica_iscritti_corso(self):
        return self.model.verifica_iscritti_corso()

    def aggiungi_iscritto_corso(self, iscritto):
        self.model.aggiungi_iscritto_corso(iscritto)

    def elimina_iscritto_corso_by_id(self, id):
        self.model.elimina_iscritto_corso_by_id(id)

    def set_tipo_corso(self, tipo):
        self.model.tipo = tipo

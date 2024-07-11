from listaingressi.model.ListaIngressi import ListaIngressi

class ControlloreListaIngressi():
    def __init__(self):
        self.model = ListaIngressi()

    def aggiungi_ingresso(self, ingresso):
        self.model.aggiungi_ingresso(ingresso)

    def rimuovi_ingresso_by_id(self, id):
        self.model.rimuovi_ingresso_by_id(id)

    def get_ingresso_by_id(self, id):
        return self.model.get_ingresso_by_id(id)

    def get_ingresso_by_index(self, index):
        return self.model.get_ingresso_by_index(index)

    def get_lista_ingressi(self):
        return self.model.get_lista_ingressi()

    def save_data(self):
        self.model.save_data()

    def get_numero_con_abbonamento(self):
        numero_con_abbonamento = 0

        if len(self.model.get_lista_ingressi()):
            for ing in self.model.get_lista_ingressi():
                if ing.tipo == "con":
                    numero_con_abbonamento += 1

        return numero_con_abbonamento

    def get_numero_senza_abbonamento(self):
        numero_senza_abbonamento = 0
        if len(self.model.get_lista_ingressi()):
            for ingr in self.model.get_lista_ingressi():
                if ingr.tipo == "senza":
                    numero_senza_abbonamento += 1

        return numero_senza_abbonamento




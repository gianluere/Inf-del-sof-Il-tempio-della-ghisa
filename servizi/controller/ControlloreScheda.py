class ControlloreScheda():
    def __init__(self, scheda):
        self.model = scheda

    def get_id_scheda(self):
        return self.model.id
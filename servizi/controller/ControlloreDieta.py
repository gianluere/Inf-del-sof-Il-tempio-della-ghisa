class ControlloreDieta:
    def __init__(self, dieta):
        self.model = dieta

    def get_id_dieta(self):
        return self.model.id
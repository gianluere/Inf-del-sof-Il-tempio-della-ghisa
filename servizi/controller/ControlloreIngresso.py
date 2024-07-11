class ControlloreIngresso():
    def __init__(self, ingresso):
        self.model = ingresso

    def get_id_ingresso(self):
        return self.model.id

    def get_tipo_ingresso(self):
        return self.model.tipo



    def set_tipo_ingresso(self, tipo):
        self.model.tipo = tipo

from ModelInterfaces.ModelInterface import ModelInterface


class ModelServer():

    def __init__(self, model_interface: ModelInterface):
        self._model_interface = model_interface

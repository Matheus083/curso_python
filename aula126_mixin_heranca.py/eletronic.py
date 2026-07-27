from log import LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._connected = False

    def connect(self):
        if not self._connected:
            self._connected = True

    def disconnect(self):
        if self._connected:
            self._connected = False

class Smartphone(Eletronic, LogFileMixin):
    def connect(self):
        super().connect()

        if self._connected:
            msg = f'{self._name} is ON.'
            self.log_sucess(msg)

    def disconnect(self):
        super().disconnect()

        if not self._connected:
            msg = f'{self._name} is ON.'
            self.log_error(msg)

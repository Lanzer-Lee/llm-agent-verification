from system.frontend import FrontEnd
from system.backend import BackEnd


class TransactionSystem:
    def __init__(self):
        self.frontend: FrontEnd | None = None
        self.backend: BackEnd | None = None
        self.setup()

    def get_frontend(self) -> FrontEnd:
        return self.frontend

    def get_backend(self) -> BackEnd:
        return self.backend

    def setup(self) -> None:
        self.backend = BackEnd()
        self.frontend = FrontEnd(self.backend)
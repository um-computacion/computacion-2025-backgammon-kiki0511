class Checker:
    """Ficha de un jugador."""
    def __init__(self, owner: str):
        self.__owner__ = owner

    def owner(self) -> str:
        return self.__owner__

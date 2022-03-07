class Pinturas:
    __idcodigo: int
    __nomedaobra: str
    __preco: str
    __artista: str

    @property
    def idcodigo(self):
        return self.__idcodigo

    @idcodigo.setter
    def idcodigo(self, idcodigo: int):
        self.__idcodigo = idcodigo

    @property
    def nomedaobra(self):
        return self.__nomedaobra

    @nomedaobra.setter
    def nomedaobra(self, nomedaobra: int):
        self.__nomedaobra = nomedaobra

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: int):
        self.__preco = preco

    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista: int):
        self.__artista = artista

    def __str__(self) -> str:
        return str(self.__class__) + ": " + str(self.__dict__)
class Docente:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
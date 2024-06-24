class Discente:
    def __init__(self, nome, sobrenome, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__matricula = matricula

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

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
from django.db import models

class Manografia:
    def __init__(self, titulo, autor, orientador, coorientador, resumo, palavras_chave, data_entrega, banca_examinadora, nota_final, area_concentracao):
        self.__titulo = titulo
        self.__autor = autor
        self.__orientador = orientador
        self.__coorientador = coorientador
        self.__resumo = resumo
        self.__palavras_chave = palavras_chave
        self.__data_entrega = data_entrega
        self.__banca_examinadora = banca_examinadora
        self.__nota_final = nota_final
        self.__area_concentracao = area_concentracao


    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def orientador(self):
        return self.__orientador

    @orientador.setter
    def orientador(self, orientador):
        self.__orientador = orientador

    @property
    def coorientador(self):
        return self.__coorientador

    @coorientador.setter
    def coorientador(self, coorientador):
        self.__coorientador = coorientador

    @property
    def resumo(self):
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo):
        self.__resumo = resumo

    @property
    def palavras_chave(self):
        return self.__palavras_chave

    @palavras_chave.setter
    def palavras_chave(self, palavras_chave):
        self.__palavras_chave = palavras_chave

    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, data_entrega):
        self.__data_entrega = data_entrega

    @property
    def banca_examinadora(self):
        return self.__banca_examinadora

    @banca_examinadora.setter
    def banca_examinadora(self, banca_examinadora):
        self.__banca_examinadora = banca_examinadora

    @property
    def nota_final(self):
        return self.__nota_final

    @nota_final.setter
    def nota_final(self, nota_final):
        self.__nota_final = nota_final

    @property
    def area_concentracao(self):
        return self.__area_concentracao

    @area_concentracao.setter
    def area_concentracao(self, area_concentracao):
        self.__area_concentracao = area_concentracao

import itertools

from model.autor import Autor
from model.categoria import Categoria
from model.editora import Editora


class Livro:
    id_iter = itertools.count(start=1)

    def __init__(self, titulo, resumo, ano, paginas, isbn, autor, categoria, editora) -> None:
        self.__id: int = next(Livro.id_iter)
        self.__titulo: str = titulo
        self.__resumo: str = resumo
        self.__ano: int = ano
        self.__paginas: int = paginas
        self.__isbn: str = isbn
        self.__autor: Autor = autor
        self.__categoria: Categoria = categoria
        self.__editora: Editora = editora

    def __str__(self) -> str:
        return f'{self.id} | {self.titulo} | {self.resumo} | {self.ano} | {self.paginas} | {self.isbn} | {self.autor.nome} | {self.categoria.nome} | {self.editora.nome}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, cat: Categoria):
        self.__categoria = cat

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, edt : Editora):
        self.__editora = edt

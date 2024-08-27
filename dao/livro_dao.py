from model.livro import Livro

class LivroDAO:
    def __init__(self) -> None:
        self.__livros: list[Livro] = []

    def listar(self) -> list[Livro]:
        return self.__livros

    def adicionar(self, livro: Livro) -> None:
        self.__livros.append(livro)

    def remover(self, livro_id: int) -> bool:
        encontrado = False
        for liv in self.__livros:
            if liv.id == livro_id:
                index = self.__livros.index(liv)
                self.__livros.pop(index)
                encontrado = True
                break

        return encontrado

    def buscar_por_id(self, livro_id) -> Livro:
        livro = None
        for liv in self.__livros:
            if liv.id == livro_id:
                livro = liv
                break
        return livro

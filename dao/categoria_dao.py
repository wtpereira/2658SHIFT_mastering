from model.categoria import Categoria

class CategoriaDAO:
    def __init__(self) -> None:
        self.__categorias: list[Categoria] = list()  # Nosso Banco de Dados

    def listar(self) -> list[Categoria]:  # SELECT * FROM categoria
        return self.__categorias

    def adicionar(self, categoria: Categoria) -> None:  # INSERT INTO categoria
        self.__categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        encontrado = False

        for cat in self.__categorias:
            if cat.id == categoria_id:
                index = self.__categorias.index(cat)
                self.__categorias.pop(index)
                encontrado = True
                break

        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if c.id == categoria_id:
                cat = c
                break

        return cat

    # def ultimo_id(self) -> int:
    #     index = len(self.__categorias) - 1
    #     if index == -1:
    #         id = 0
    #     else:
    #         id = self.__categorias[index].id

    #     return id

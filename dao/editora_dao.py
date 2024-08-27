from model.editora import Editora

class EditoraDAO:

    def __init__(self):
        self.__editoras: list[Editora] = list()

    def listar(self) -> list[Editora]:
        return self.__editoras

    def adicionar(self, editora: Editora) -> None:
        self.__editoras.append(editora)

    def remover(self, editora_id: int) -> bool:
        encontrado = False
        for e in self.__editoras:
            if (e.id == editora_id):
                index = self.__editoras.index(e)
                self.__editoras.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, editora_id) -> Editora:
        edt = None
        for e in self.__editoras:
            if (e.id == editora_id):
                edt = e
                break
        return edt

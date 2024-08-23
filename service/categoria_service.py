from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria

class CategoriaService:
    def __init__(self) -> None:
        self.__categoria_dao: CategoriaDAO = CategoriaDAO()

    def menu(self):
        print('[Categoria] Escolha uma das seguintes opções: \n'
              '1 - Listar todas as categorias\n'
              '2 - Adicionar nova categoria\n'
              '3 - Excluir categoria\n'
              '4 - Ver categoria por ID\n'
              '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        match escolha:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                self.adicionar()
            case '3':
                self.remover()
            case '4':
                self.mostar_por_id()
            case _:
                print('Opção inválida. Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('Listando categorias...')
        categorias = self.__categoria_dao.listar()
        if len(categorias) == 0:
            print('Nenhuma categoria encontrada!')

        for categoria in categorias:
            print(categoria)

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('Adicionando categoria...')
        nome = input('Digite o nome da categoria de livro: ')
        # id = self.__categoria_dao.ultimo_id() + 1
        # nova_categoria = Categoria(id, nome)
        nova_categoria = Categoria(nome)
        self.__categoria_dao.adicionar(nova_categoria)
        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('Removendo categoria...')
        categoria_id = int(input('Digite o ID da categoria para excluir: '))
        if self.__categoria_dao.remover(categoria_id):
            print('Categoria excluída com sucesso!')
        else:
            print('Categoria não encontrada!')

        input('Pressione uma tecla para continuar...')

    def mostar_por_id(self):
        print('Mostrar categoria por ID...')
        categoria_id = int(input('Digite o ID da categoria para buscar: '))
        cat = self.__categoria_dao.buscar_por_id(categoria_id)

        if cat:
            print(cat)
        else:
            print('Categoria não encontrada!')

        input('Pressione uma tecla para continuar...')


if __name__ == '__main__':
    service = CategoriaService()
    service.menu

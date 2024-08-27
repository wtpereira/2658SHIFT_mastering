from dao.livro_dao import LivroDAO
from dao.autor_dao import AutorDAO
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO

from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from model.livro import Livro


class LivroService:
    livro_dao: LivroDAO = LivroDAO()

    def __init__(self) -> None:
        self.__autor_dao: AutorDAO = AutorService.autor_dao
        self.__categoria_dao: CategoriaDAO = CategoriaService.categoria_dao
        self.__editora_dao: EditoraDAO = EditoraService.editora_dao

    def menu(self):
        print('[Livros] Escolha uma das seguintes opções:\n'
                '1 - Listar todos os livros\n'
                '2 - Adicionar novo livro\n'
                '3 - Excluir livro\n'
                '4 - Ver livro por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')

        match escolha:
            case '0':
                return
            case '1':
                self.listar()
            case '2':
                if self.__autor_dao.listar() and self.__categoria_dao.listar() and self.__editora_dao.listar():
                    self.adicionar()
                else:
                    print('Dados insuficientes para cadastrar um livro!')

            case '3':
                self.remover()
            case '4':
                self.mostrar_por_id()
            case _:
                print('Opção inválida! Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('Listando livros...')

        livros = LivroService.livro_dao.listar()
        if len(livros) == 0:
            print('Nenhum livro encontrado!')

        for livro in livros:
            print(livro)

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('Adicionando livro...')
        try:
            titulo = input('Digite o título do livro: ')
            resumo = input('Digite o resumo do livro: ')
            ano = int(input('Digite o ano do livro: '))
            paginas = int(input('Digite a quantidade de páginas do livro: '))
            isbn = input('Digite o ISBN do livro: ')

            print('Autores de livro:')
            lista_autores = self.__autor_dao.listar()
            for autor in lista_autores:
                print(autor)

            id_autor = int(input('Digite o ID do autor do livro: '))

            autor = self.__autor_dao.buscar_por_id(id_autor)

            print('Categorias de Livros:')
            lista_categorias = self.__categoria_dao.listar()
            for cat in lista_categorias:
                print(cat)

            id_categoria = int(input('Digite o ID da categoria do livro: '))
            categoria = self.__categoria_dao.buscar_por_id(id_categoria)

            print('Editoras de Livros:')
            lista_editoras = self.__editora_dao.listar()
            for edt in lista_editoras:
                print(edt)

            id_editora = int(input('Digite o ID da editora do livro: '))
            editora = self.__editora_dao.buscar_por_id(id_editora)

            livro = Livro(titulo, resumo, ano, paginas, isbn, autor, categoria, editora)

            self.livro_dao.adicionar(livro)
        except Exception as e:
            print(f'Erro ao adicionar livro! - {e}')

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('Removendo livro...')
        livro_id = int(input('Digite o ID do livro para excluir: '))
        if LivroService.livro_dao.remover(livro_id):
            print('Livro excluído com sucesso!')
        else:
            print('Livro não encontrado!')

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\Livro por Id...')

        try:
            id = int(input('Digite o Id do livro para buscar: '))
            livro = LivroService.livro_dao.buscar_por_id(id)

            if livro:
                print(livro)
            else:
                print('Livro não encontrado!')
        except Exception as e:
            print(f'Erro ao exibir Livro! - {e}')
            return

        input('Pressione uma tecla para continuar...')
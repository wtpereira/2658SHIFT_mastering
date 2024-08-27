from service.autor_service import AutorService
from service.categoria_service import CategoriaService
from service.editora_service import EditoraService
from service.livro_service import LivroService

autor_service = AutorService()
categoria_service = CategoriaService()
editora_service = EditoraService()
livro_service = LivroService()


def menu_principal():
    print('[Menu Principal] Escolha uma das seguintes opções:\n'
            '1 - Categorias\n'
            '2 - Editoras\n'
            '3 - Autores\n'
            '4 - Livros\n'
            '0 - Sair do programa\n')
    escolha = input('Digite a opção: ')

    match escolha:
        case '0':
            print('Obrigado, até logo!')
            return
        case '1':
            categoria_service.menu()
        case '2':
            editora_service.menu()
        case '3':
            autor_service.menu()
        case '4':
            livro_service.menu()
        case _:
            print('Opção inválida! Por favor, tente novamente!')

    menu_principal()


if __name__ == '__main__':
    menu_principal()

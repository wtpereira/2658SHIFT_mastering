from dao.autor_dao import AutorDAO
from model.autor import Autor

class AutorService:
    autor_dao: AutorDAO = AutorDAO()

    def menu(self):
        print('[Autores] Escolha uma das seguintes opções:\n'
                '1 - Listar todas os autores\n'
                '2 - Adicionar novo autor\n'
                '3 - Excluir autor\n'
                '4 - Ver autor por Id\n'
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
                self.mostrar_por_id()
            case _:
                print('Opção inválida. Por favor, tente novamente!')

        self.menu()

    def listar(self):
        print('\nListando autores...')

        try:
            autores = AutorService.autor_dao.listar()
            if len(autores) == 0:
                print('Nenhum autor encontrado!')

            for autor in autores:
                print(f'{autor.id} | {autor.nome} | {autor.email} | {autor.telefone} | {autor.bio}')
        except Exception as e:
            print(f'Erro ao exibir os autores! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando autor...')

        try:
            nome = input('Digite o nome do autor: ')
            email = input('Digite o email do autor: ')
            telefone = input('Digite o telefone do autor: ')
            bio = input('Digite uma bio reduzida do autor: ')
            novo_autor = Autor(nome, email, telefone, bio)
            AutorService.autor_dao.adicionar(novo_autor)
            print('Autor adicionado com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo autor...')

        try:
            autor_id = int(input('Digite o ID do autor para excluir: '))
            if (AutorService.autor_dao.remover(autor_id)):
                print('Autor excluído com sucesso!')
            else:
                print('Autor não encontrado!')
        except Exception as e:
            print(f'Erro ao excluir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\nAutor por Id...')

        try:
            id = int(input('Digite o Id do autor para buscar: '))
            aut = AutorService.autor_dao.buscar_por_id(id)

            if aut:
                print(aut)
            else:
                print('Autor não encontrado!')
        except Exception as e:
            print(f'Erro ao exibir autor! - {e}')
            return

        input('Pressione uma tecla para continuar...')
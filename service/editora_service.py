from dao.editora_dao import EditoraDAO
from model.editora import Editora

class EditoraService:
    editora_dao: EditoraDAO = EditoraDAO()

    def menu(self):
        print('[Editoras] Escolha uma das seguintes opções:\n'
                '1 - Listar todas as editoras\n'
                '2 - Adicionar nova editora\n'
                '3 - Excluir editora\n'
                '4 - Ver categoria por Id\n'
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
        print('\nListando editoras...')

        try:
            editoras = EditoraService.editora_dao.listar()
            if len(editoras) == 0:
                print('Nenhuma editora encontrada!')

            for editora in editoras:
                print(f'{editora.id} | {editora.nome} | {editora.endereco} | {editora.telefone}')
        except Exception as e:
            print(f'Erro ao exibir as editoras! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def adicionar(self):
        print('\nAdicionando editora...')

        try:
            nome = input('Digite o nome da editora: ')
            endereco = input('Digite o endereço da editora: ')
            telefone = input('Digite o telefone da editora: ')
            nova_editora = Editora(nome, endereco, telefone)

            EditoraService.editora_dao.adicionar(nova_editora)
            print('Editora adicionada com sucesso!')
        except Exception as e:
            print(f'Erro ao inserir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def remover(self):
        print('\nRemovendo editora...')

        try:
            editora_id = int(input('Digite o ID da excluir para excluir: '))
            if (EditoraService.editora_dao.remover(editora_id)):
                print('Editora excluída com sucesso!')
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao excluir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

    def mostrar_por_id(self):
        print('\Editora por Id...')

        try:
            id = int(input('Digite o Id da editora para buscar: '))
            edt = EditoraService.editora_dao.buscar_por_id(id)

            if edt:
                print(edt)
            else:
                print('Editora não encontrada!')
        except Exception as e:
            print(f'Erro ao exibir editora! - {e}')
            return

        input('Pressione uma tecla para continuar...')

def verifica_se_e_true(contatos, indice_contato):
    return len(contatos) > 0 and len(contatos) >= indice_contato

def adicionar_contato(nome, telefone, email):
    if nome and telefone and email:
        novo_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
        contatos.append(novo_contato)
        print(len(contatos))
    return

def visualizar_lista_contato(contatos):
    if len(contatos) > 0:
        for indice, contato in enumerate(contatos, start=1):
            print(f'\nContato {indice}\nNome: {contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']}\nFavorito: {contato['favorito']}\n')
    else:
        print('Você não possui nenhum contato! :(')
    return

def editar_contato(contatos, indice_do_contato):
    if verifica_se_e_true(contatos, indice_do_contato):
        contatos[indice_do_contato - 1]['nome'] = input('Digite o novo nome: ')
        contatos[indice_do_contato - 1]['telefone'] = input('Digite o novo telefone: ')
        contatos[indice_do_contato - 1]['email'] = input('Digite o novo e-mail: ')
        print(f'Contato: {contatos[indice_do_contato - 1]['nome']} alterado com sucesso!')
        

def marcar_contato_como_favorito(contatos, indice_do_contato):
    if verifica_se_e_true(contatos, indice_do_contato):
        contato = contatos[indice_do_contato - 1]
        if contato['favorito'] == False:
            contato['favorito'] = True
        else:
            contato['favorito'] = False

        favorito = 'foi marcado como favorito' if contato['favorito'] else 'foi desmarcado como favorito.'
        print(f'Contato: {contato['nome'].upper()} {favorito}')
    return

def visualizar_contatos_favoritos(contatos):
    for contato in contatos:
        if contato['favorito']:
            print(f'\nNome: {contato['nome']}\nTelefone: {contato['telefone']}\nE-mail: {contato['email']}\n')
    return

def excluir_contato(contatos, indice_do_contato):
    if verifica_se_e_true(contatos, indice_do_contato):
        print(f'Contato {contatos[indice_do_contato - 1]['nome'].upper()} removido com sucesso!')
        contatos.remove(contatos[indice_do_contato - 1])
    return


contatos = []
while True:
        print('\nAgenda de contatos')
        print('1. Adicionar um contato')
        print('2. Visualizar lista de contatos')
        print('3. Editar um contato')
        print('4. Marcar/Desmarcar contato como Favorito')
        print('5. Visualizar contatos Favortos')
        print('6. Apagar contato')
        print('7. Sair da Agenda')

        opcao_usuario = int(input('Digite a opção desejada: '))
        
        if opcao_usuario == 7:
            print('Você saiu da agenda. :D')
            break

        if opcao_usuario == 1:
            nome = input('Nome do contato: ')
            telefone = input('Telefone do contato: ')
            email = input('E-mail do contato: ')
            adicionar_contato(nome, telefone, email)

        if opcao_usuario == 2:
            visualizar_lista_contato(contatos)

        
        if opcao_usuario == 3:
            indice_do_contato = int(input('Digite o índice do contato que deseja editar: '))
            editar_contato(contatos, indice_do_contato)

        if opcao_usuario == 4:
            indice_do_contato = int(input('Digite o índice que deseja marcar como favorito: '))
            marcar_contato_como_favorito(contatos, indice_do_contato)

        if opcao_usuario == 5:
            visualizar_contatos_favoritos(contatos)

        if opcao_usuario == 6:
            indice_do_contato = int(input('Digite o índice do contato que deseja remover: '))
            excluir_contato(contatos, indice_do_contato)
    
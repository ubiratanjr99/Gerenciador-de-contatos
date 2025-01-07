'''
- Objetivo: biblioteca "os" vai ser usada pra limpar os dados do terminal ('cls') e a biblioteca "time" vai ser usada pra colocar um intervalo de tempo
entre a execução de determinadas funções.
'''
import os
import time

'''
- Objetivo: lista de dicionários que representam cadastros de contatos.
'''
# Lista de dicionários
contatos = [
    {'nome': 'Maria dos Santos', 'telefone': 11912345678, 'email': 'maria@gmail.com'},
    {'nome': 'João de Almeida', 'telefone': 1114253647, 'email': 'joao@gmail.com'},
    {'nome': 'Gabriel de Souza', 'telefone': 11987654321, 'email': 'gabriel@gmail.com'}
]

def escolher_opcao(opcao_escolhida):

    '''
    - Objetivo: função principal. Ela que vai chamar as outras dentro de uma estrutura conficional. 
    Back-End da tela principal do console.
    - Inputs: nenhum.
    '''
    # a variável "opcao_escolhida" foi passada como parâmetro da função pra que eu possa referenciar ela dentro dessa função.
    # P.S.: em Python, variáveis de uma função são locais, pra chamar em outras funções tem que colocar como parâmetro ou deixar global.
    try:
        if opcao_escolhida == 1:
            add_contact()
        elif opcao_escolhida == 2:
            delete_contact()
        elif opcao_escolhida == 3:
            pesquisar()
        elif opcao_escolhida == 4:
            list_contacts()
        elif opcao_escolhida == 5:
            os.system('cls')
            print('Finalizando programa...')
            time.sleep(1.25)
            os.system('cls')
        else:
            opcao_invalida()
            show_options()
            
    except:
        opcao_invalida()
        show_options()    

def buscando():  
    '''
    - Objetivo: criar uma "animação" antes de exibir as lista de contatos cadastrados.
    '''
    os.system('cls')
    print('Buscando.')
    time.sleep(0.25)
    os.system('cls')
    print('Buscando..')
    time.sleep(0.25)
    os.system('cls')
    print('Buscando...')
    time.sleep(0.25)
    os.system('cls')
    print('Buscando.')
    time.sleep(0.25)
    os.system('cls')
    print('Buscando..')
    time.sleep(0.25)
    os.system('cls')
    print('Buscando...')
    time.sleep(0.25)
    os.system('cls')

def show_title():
    print("""
█░░ █ █▀ ▀█▀ ▄▀█   █▀▄ █▀▀   █▀▀ █▀█ █▄░█ ▀█▀ ▄▀█ ▀█▀ █▀█ █▀
█▄▄ █ ▄█ ░█░ █▀█   █▄▀ ██▄   █▄▄ █▄█ █░▀█ ░█░ █▀█ ░█░ █▄█ ▄█ \n""")

def show_options():
    '''
    - Objetivo: armazenar na variável "opcao_escolhida" o input do usuário pra depois utilizar essa mesma variável
    na estrutura condicional da função "escolher_opcao()"
    - Inputs: opção escolhida.
    '''
    os.system('cls')
    show_title()

    print('1. Adicionar novo')
    print('2. Excluir')
    print('3. Pesquisar')
    print('4. Listar todos')
    print('5. Sair\n')

    opcao_escolhida = int(input('Digite a opção escolhida: '))
    escolher_opcao(opcao_escolhida)

def opcao_invalida():
    '''
    - Objetivo: exibir uma mensagem de "Opção inválida" quando o usuário colocar um input que não condiz com as opções listadas.
    '''
    os.system('cls')
    print('Opção inválida!')
    time.sleep(1.5)
    os.system('cls')

def delete_contact():
    '''
    - Objetivo: identificar se um valor de chave existe em algum dos dicionários e caso exista, excluir todo o dicionário onde esse valor se encontra.
    - Inputs: meio de busca, confirmar se deseja mesmo excluir, voltar pro menu principal.
    '''
    os.system('cls')
    print('Selecione como deseja realizar a busca:\n')
    print('1. Telefone')
    print('2. E-mail')
    print('3. Voltar para o menu principal')

    escolha_tipo_contato = int(input('\nDigite a forma de busca: '))

    if escolha_tipo_contato == 1:
        os.system('cls')
        telefone = int(input('Digite o telefone (apenas os números): '))

        os.system('cls')
        print(f'Tem certeza que deseja excluir o contato "{telefone}"?\n\n1. Sim\n2. Não\n')
        confirmacao = int(input('Escolha: '))

        if confirmacao == 1:
            encontrado = False
            for contato in contatos:
                if contato['telefone'] == telefone:
                    contatos.remove(contato)
                    os.system('cls')
                    print(f'O contato "{contato["nome"]}" de telefone "{telefone}" foi excluído com sucesso!')
                    encontrado = True
                    input('\nAperte qualquer tecla para voltar pro menu de exclusão ')
                    delete_contact()
                    break

            if not encontrado:
                os.system('cls')
                print('Telefone não encontrado!')
                time.sleep(2)
                delete_contact()

        elif confirmacao == 2:
            os.system('cls')
            print('Voltando para o menu de exclusão...')
            time.sleep(2)
            delete_contact()

    elif escolha_tipo_contato == 2: 
        os.system('cls')
        email = str(input('Digite o e-mail: '))

        os.system('cls')
        print(f'Tem certeza que deseja excluir o contato {email}?\n\n1. Sim\n2. Não\n')
        confirmacao = int(input(f'Escolha: '))

        if confirmacao == 1:
            encontrado = False
            for contato in contatos:
                if contato['email'] == email:
                    contatos.remove(contato)
                    os.system('cls')
                    print(f'O contato "{contato["nome"]}" de e-mail "{email}" foi excluído com sucesso!')
                    encontrado = True
                    input('\nAperte qualquer tecla para voltar pro menu de exclusão ')
                    delete_contact()
                    break

            if not encontrado:
                os.system('cls')
                print('E-mail não encontrado!')
                time.sleep(2)
                delete_contact()

        elif confirmacao == 2:
            print('Voltando para o menu de exclusão...')
            time.sleep(2)
            show_options()

    elif escolha_tipo_contato == 3:
        os.system('cls')
        show_options()
    else:
        opcao_invalida()
        show_options()

def list_contacts():
    '''
    - Objetivo: listar todos os contatos cadastrados até o momento.
    - Input: input simples apenas para acionar a função "show_options()" que vai levar de volta pro meni principal.
    '''
    buscando()
    for contato in contatos:
        print(f'Nome: {contato["nome"]}\nTelefone: {contato["telefone"]}\nE-mail: {contato["email"]}\n')
    
    str(input('Aperte qualquer tecla para voltar pro menu principal '))
    show_options()

def pesquisar():
    '''
    - Objetivo: consultar um  ontato completo (nome, e-mail e telefone) apenas informando o valor de uma das chaves do dicionário (telefone ou e-mail).
    '''
    os.system('cls')
    pesquisa = int(input('Deseja pesquisar por:\n\n1. E-mail\n2. Telefone\n3. Sair\n\nDigite sua escolha: '))

    existe = False

    if pesquisa == 1:

        os.system('cls')
        email = str(input('Digite o e-mail: '))

        for contato in contatos:
            if contato['email'] == email:
                os.system('cls')
                print('Resultado da pesquisa:\n')
                print(f'Nome: {contato["nome"]}\nTelefone: {contato["telefone"]}\nE-mail: {contato["email"]}')
                existe = True
                input('\nDigite qualquer tecla para voltar ao menu de pesquisa ')
                pesquisar()
                
        if not existe:
            os.system('cls')
            print('E-mail não encontrado!')
            time.sleep(2)
            pesquisar()


    elif pesquisa == 2:

        try: 
            os.system('cls')
            telefone = int(input('Digite o telefone (apenas os números): '))

            for contato in contatos:
                if contato['telefone'] == telefone:
                    os.system('cls')
                    print('Resultado da pesquisa:\n')
                    print(f'Nome: {contato["nome"]}\nTelefone: {contato["telefone"]}\nE-mail: {contato["email"]}')
                    existe = True
                    input('\nDigite qualquer tecla para voltar ao menu de pesquisa ')
                    pesquisar()
        except ValueError:
            if not existe:
                os.system('cls')
                print('Telefone não encontrado!')
                time.sleep(2)
                pesquisar()

    elif pesquisa == 3:
        show_options()
    else:
        opcao_invalida()
        pesquisar()
    
def add_contact():

    ''' 
    - Objetivo: adicionar um novo dicionário (novo usuário) na lista. 
    - Inputs: nome completo, telefone e e-mail. 
    '''

    os.system('cls')
    nome = str(input('Nome completo: '))
    telefone = int(input('Telefone/Celular (apenas os números): '))
    email = str(input('E-mail: '))

    os.system('cls')
    print(f'Deseja adicionar "{nome}"?')
    confirm_contact = int(input('\n1. Sim\n2. Digitar novamente\n3. Sair\n\nEscolha: '))

    if confirm_contact == 1:

        # Vai salvar os dados preenchidos na váriavel e adicionar ao dicionário (contatos).
        dados_contato = {'nome': nome, 'telefone': telefone, 'email': email}
        contatos.append(dados_contato)

        os.system('cls')
        print('Contato salvo com sucesso!\n')
        time.sleep(2)
        os.system('cls')
        show_options()

    elif confirm_contact == 2:
        add_contact()

    else:
        # Retorna pra função de adicionar contato.
        show_options()

show_options()

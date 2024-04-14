# implementacoes baseadas no codigo da DIO
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nc] Novo cliente
[nr] Nova conta corrente
[lc] Listar clientes
[lr] Listar contas correntes
[q] Sair

=> """

saldo = 0
valor = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

quantidade_contas = 0
contas_cliente = []
contas_corrente = []

def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f'Depósito realizado no valor de R$ {valor:.2f}.')
        return saldo, extrato

    else:
        print("O valor informado é inválido.")

def saque(*, saldo, valor, extrato, limite, LIMITE_SAQUES, numero_saques):

    if valor > saldo:
        print('Voce nao possui saldo suficiente para esta operacao.')

    elif valor > limite:
        print('O valor inserido excede o limite máximo de saques. Tente novamente.')

    elif numero_saques > LIMITE_SAQUES:
        print('O limite de saques diários foi excedido. Tente novamente mais tarde.')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Saque realizado no valor de R$ {valor:.2f}.')
        return saldo, extrato, numero_saques
    
    else:
        print('Valor inválido. Tente novamente.')

def exibir_extrato(saldo, /, *, extrato,):

    print("\n================ EXTRATO ================\n")
    
    if extrato == '':
        print('Não foram realizadas movimentações.\n')
    else:
        print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}\n')
    
    print("==========================================")

def criar_conta(contas_cliente):
    print('Para criar sua conta, responda as informações abaixo:\n')

    nome = str(input('Digite seu Nome: '))
    nome = nome.capitalize()
    data_nascimento = str(input('Digite sua Data de Nascimento: '))
    cpf = ''
    while cpf == '':
        cpf = str(input('Digite seu CPF (somente dígitos): '))
        if cpf == '' or len(cpf) != 11:
            print('CPF inválido. Tente novamente.')
            cpf = ''
    endereco = str(input('Digite seu endereço: '))

    cliente = {'nome': nome, 'cpf': cpf}
    contas_cliente.append(cliente)

    return contas_cliente

def criar_conta_corrente(contas_cliente, quantidade_contas, contas_corrente):
    
    cpf = input('Digite seu CPF:')
    for cliente in contas_cliente:
        if cpf == cliente['cpf']:
            cpf_valido = True
            nome = cliente['nome']
            print('Olá, ' + nome + '!')
    
    if cpf_valido:
        sn = input('Deseja criar uma nova conta? (S/N) ')
        if sn == 's' or sn == 'S':
            quantidade_contas += 1
            conta = {'numero_conta': quantidade_contas, 'usuario': cpf, 'nome': nome}
            contas_corrente.append(conta)
            print(f'Conta {conta["numero_conta"]} criada com sucesso!')
    
    if not cpf_valido:
        print('CPF não encontrado. Tente novamente ou crie uma nova conta.')

    return quantidade_contas, contas_corrente

def listar_contas_cliente(contas_cliente):

    print('Lista de clientes cadastrados:\n')

    for cliente in contas_cliente:
        print(cliente['nome'])

def listar_contas_corrente(contas_corrente):

    print('Lista de contas corrente cadastradas:\n')

    for cliente in contas_corrente:
        print('0001-' + str(cliente['numero_conta']) + ' - ' + cliente['nome'])




while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, LIMITE_SAQUES=LIMITE_SAQUES, numero_saques=numero_saques)

    elif opcao == "e":

        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 'nc':
        
        contas_cliente = criar_conta(contas_cliente)

    elif opcao == 'nr':

        quantidade_contas, contas_corrente = criar_conta_corrente(contas_cliente, quantidade_contas, contas_corrente)

    elif opcao == 'lc':

        listar_contas_cliente(contas_cliente)

    elif opcao == 'lr':

        listar_contas_corrente(contas_corrente)

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")

menu = '''
    ========= MENU =========
    
        [d] = depositar
        [s] = saque
        [e] = extrato
        [0] = sair
    
    =========================
'''

saldo = 0
extrato = []
saques_dia = 0
LIMITE_SAQUES = 3

def deposito(valor):

    global saldo
    global extrato

    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito de R$ {valor:.2f}')
        print(f'depósito realizado no valor de R$ {valor:.2f}')
    else:
        print('valor inválido. tente novamente')

def saque(valor):

    global saldo
    global saques_dia
    global extrato

    if not saques_dia > LIMITE_SAQUES:
        if valor > 0 and valor <= 500:
            if saldo >= valor:
                saldo -= valor
                saques_dia += 1
                print(f'saque realizado no valor de R$ {valor:.2f}')
                extrato.append(f'Saque de R$ {valor:.2f}')
            else: 
                print('saldo insuficiente. tente novamente')
        else:
            print('valor inválido. tente novamente')
    else:
        print('o seu limite diário de saques foi atingido. tente novamente outro dia')

def print_extrato():
    
    global extrato

    if not extrato == []:
        print('''
    ========= EXTRATO =========
    ''')
        
        for action in extrato:

            print('     ' + action)

        print(f'     Saldo atual: R$ {saldo:.2f}')
    else:
        print('Não foram realizadas movimentações.')

run = True

while run:

    opcao = input(menu)

    match opcao:

        case 'd':

            valor = float(input('digite o valor do depósito: '))
            deposito(valor)
        
        case 's':

            valor = float(input('digite o valor do saque: '))
            saque(valor)

        case 'e':

            print_extrato()

        case '0':

            run = False

        case _:

            print('opcao invalida. tente novamente')
            






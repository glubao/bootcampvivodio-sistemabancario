from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print('Operação não realizada. Valor inserido é inválido.')
            return False

        if valor > self._saldo:
            print('Operação não realizada. Saldo insuficiente.')
            return False

        self._saldo -= valor
        print('\nSaque realizado com sucesso.')
        return True

    def depositar(self, valor):
        if valor <= 0:
            print('Operação não realizada. Valor inserido é inválido.')
            return False

        self._saldo += valor
        print('\nDepósito realizado com sucesso.')
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite_diario=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite_diario = limite_diario
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == 'Saque'])

        if valor > self._limite_diario:
            print('Operação não realizada. Limite diário excedido.')
            return False

        if numero_saques >= self._limite_saques:
            print('Operação não realizada. Limite de saques diários excedido.')
            return False

        return super().sacar(valor)

    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            Conta:\t\t{self.numero}
            Titular:\t{self._cliente.nome}
        '''


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
        )


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @abstractproperty
    def valor(self):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


def menu():
    menu = """
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # Listar todas as contas do cliente
    print("\nContas do cliente:")
    for i, conta in enumerate(cliente.contas, 1):
        print(f"{i}. {conta.numero}")

    # Pedir ao usuário para escolher uma conta
    escolha = int(input("Escolha o número da conta: "))
    if escolha < 1 or escolha > len(cliente.contas):
        print("\n@@@ Escolha inválida! @@@")
        return

    return cliente.contas[escolha - 1]


def depositar(clientes):
    cpf = input('Informe o CPF do cliente destino: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado.')
        return

    valor = float(input('Informe o valor do depósito: '))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado.')
        return

    valor = float(input('Informe o valor do saque: '))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado.')
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================\n")
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        print('Não foram realizadas movimentações.\n')
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\nData: {transacao['data']}"

    print(extrato)
    print(f"\nSaldo:\t R$ {conta.saldo:.2f}")
    print("==========================================")


def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado.')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta criada com sucesso.')


def criar_cliente(clientes):
    cpf = input('Digite seu CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\nJá existe um cliente com esse CPF.')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print('\nCliente criado com sucesso.')


def listar_contas(clientes):
    for cliente in clientes:
        print(f'Contas de {cliente.nome}:\n')
        for conta in cliente.contas:
            print("=" * 100)
            print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'lc':
            listar_contas(clientes)

        elif opcao == 'lr':
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")


main()

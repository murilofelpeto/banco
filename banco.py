#Banco

from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos PRIVADOS:
    - nome,
    - telefone,
    - email.
    caso o email não seja válido (verificar se contém o @) gera um ValueError,
    caso o telefone não seja um número inteiro gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome

        if(type(telefone) is int):
            self.__telefone = telefone
        else:
            raise TypeError("Telefone inválido")
        if "@" in email:
            self.__email = email
        else:
            raise ValueError("Email inválido!")

    def get_nome(self) -> str:
        return self.__nome

    def get_telefone(self) -> int:
        return self.__telefone

    def set_telefone(self, novo_telefone: int) -> None:
        if(type(novo_telefone) is int):
            self.__telefone = novo_telefone
        else:
            raise TypeError("Telefone inválido")

    def get_email(self) -> str:
        return self.__email

    def set_email(self, novo_email: str) -> None:
        if "@" in novo_email:
            self.__email = novo_email
        else:
            raise ValueError("Email inválido!")


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    - abre_conta(): abre uma nova conta, atribuindo o numero da conta em ordem
    crescente a partir de 1 para a primeira conta aberta.
    - lista_contas(): apresenta um resumo de todas as contas do banco

    DICA: crie uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    __contas = list()
    __numero_conta = 0

    def __init__(self, nome: str):
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
        e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """
        pass
        if saldo_ini >= 0:
            self.__numero_conta = self.__numero_conta + 1
            conta = Conta(clientes, self.__numero_conta, saldo_ini)
            self.__contas.append(conta)
        else:
            raise ValueError("Saldo inicial inválido")

    def lista_contas(self) -> List['Conta']:
        return self.__contas


class Conta():
    """
    Classe Conta:
    - Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito', 200) etc.
    - Caso o saldo inicial seja menor que zero deve lançar um ValueError
    - A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)

    DICA: Crie uma variável interna privada para guardar as
    operações feitas na conta
    """
    __clientes = list()
    __historico = list()

    def __init__(self, clientes: List[Cliente],
                 numero_conta: int,
                 saldo_inicial: Number):
        for cliente in clientes:
            self.__clientes.append(cliente)
            self.__saldo = saldo_inicial
            self.__numero_conta = numero_conta
            self.__addHistorico("saldo_inicial", saldo_inicial)

    def get_clientes(self) -> List[Cliente]:
        return self.__clientes

    def get_saldo(self) -> Number:
        return self.__saldo

    def get_numero(self) -> int:
        return self.__numero_conta

    def saque(self, valor: Number) -> None:
        if(self.__saldo > valor):
            self.__saldo = self.__saldo - valor
            self.__addHistorico("saque", valor)
        else:
            raise ValueError("Saldo insuficiente")

    def deposito(self, valor: Number):
        self.__saldo = self.__saldo + valor
        self.__addHistorico("deposito", valor)

    def extrato(self) -> List[Dict[str, Number]]:
        return self.__historico

    def __addHistorico(self, operacao: str, valor: Number):
        extrato = [{operacao: valor}]
        self.__historico.append(extrato)

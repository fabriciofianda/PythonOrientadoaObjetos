#Entendendo Orientação a Objetos em Python
Esse repositório contém o código utilizado no curso de Orientação a Objetos em Python, onde aprendemos sobre os principais conceitos da programação orientada a objetos utilizando a linguagem Python.

Conteúdo
No código presente neste repositório, criamos uma classe Conta que representa uma conta bancária. Através desta classe, podemos realizar diversas operações bancárias, como depósitos, saques, transferências e consultas de saldo.

Métodos e Atributos
Na criação da classe Conta, utilizamos os seguintes métodos e atributos:

Atributos
__numero: número da conta bancária (privado)
__titular: nome do titular da conta bancária (privado)
__saldo: saldo atual da conta bancária (privado)
__limite: limite de crédito da conta bancária (privado)
__codigo_banco: código do banco da conta bancária (privado)
Métodos
extrato(): exibe o saldo da conta bancária e o nome do titular
depositar(valor): adiciona um valor ao saldo da conta bancária
__pode_retirar(valor_de_saque): verifica se é possível realizar um saque na conta bancária
retirar(valor): realiza um saque na conta bancária
transferir(valor, origem, destino): transfere um valor de uma conta bancária para outra
@property
@property.setter
@staticmethod
Funcionamento do código
Ao criar uma instância da classe Conta, é possível realizar diversas operações bancárias. Além disso, também podemos consultar informações da conta, como saldo e número da conta, utilizando os métodos saldo() e numero().

Também é possível modificar o limite de crédito da conta bancária utilizando o método limite().
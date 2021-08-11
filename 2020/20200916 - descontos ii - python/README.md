## Em Video
Voce pode assistir a esta sessão em:
* https://youtu.be/cdH5rFkUOpg

# Problema

Crie um programa que retorne melhor valor possível de valor não tributado para uma empresa no simples (ME) com um único sócio.

As regras de tarifação para pessoa física estão em um outro dojo que realizamos: https://github.com/dojorio/dojolive/blob/master/2020/20200715%20-%20descontos%20-%20python/descontos_test.py

Para pessoa jurídica, na primeira faixa do simples (teto de 180.000/ano, 15.000/mês) uma empresa de consultoria em TI pode ficar enquadrada em dois anexos diferentes:

Anexo V: Ele paga 15,5% de impostos na DAS baseados no faturamento total do mês

Anexo III: Paga 6% de impostos sobre o faturamento total do mês.

O que define o anexo a ser tarifado é o fator R.
O fator R é basicamente um cálculo entre quanto a empresa gasta com folha de pagamentos e o quanto ela fatura, no caso de uma empresa com um sócio, o fator R é definido por: pró-labore/faturamento do mês.

Para a empresa ficar no anexo III o fator R dos últimos 12 meses precisa ser maior ou igual a 28%.

O pró-labore do sócio é calculado da mesma forma que se calcula um salário de uma pessoa física, tendo a alíquota de 11% pro INSS fixa (respeitando o teto do INSS)


## Participantes

1. Daniel Drumond (o cliente, de Floripa)
2. Chico Lucio (Niterói)
3. Cláudio Berrondo (Rio de Janeiro)
4. Celestino Gomes (o único, original! - Rio de Janeiro)
5. Leo (Belém)
6. Fabricio Vieira (Salvador)

## Retrospectiva

### 😀

- Repl.it menos instável
- Novo integrante (Bem vindo Fabricio)
- Usamos um "dojo" antigo como biblioteca

### 😩

- O Leo caiu
- O Repl.it ainda travou
- Decimal não faz precisão decimal de forma simples
- (Tino) Fiquei preocupado se preciso recolher prolabore ou não

### 🤫

- dojo seriado?... vai ter a teceira temporada?... contrato com a Netflix...
- Usar o Zoom? Claudio?
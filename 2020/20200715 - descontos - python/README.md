
# Problema

Monte um programa que calcule o salário líquido de um trabalhador CLT, levando em consideração apenas a contribuição para o INSS e o desconto em folha do IRPF.

Um trabalhador CLT paga as seguintes taxas em folha de pagamento:

INSS:
Até 1045        | 7,5% | -
1045,01-2089,60 |  9%  | 15,67
2089,61-3134,40 | 12%  | 78,36
3134,41-6101,06 | 14%  | 141,05

6101,06 é o teto do INSS, tudo o que passa desse valor o trabalhador não paga, ou seja, se ele ganha 7000 reais ele irá pagar apenas 14% em cima de 6101,06 - 141,05

Ou seja, se o trabalhador ganha 5000 reais ele irá pagar de INSS:
5000*14%-141,05=558,95.

IRPF:
  Base de cálculo     | Alíquota |  Dedução
Até 1.903,98          |  Isento  |  Isento
1.903,99-2.826,65     |   7,5    |  142,80
De 2.826,66-3.751,05  |    15    |  354,80
De 3.751,06-4.664,68  |   22,5   |  636,13
Acima de 4.664,68     |   27,5   |  869,36


Com a seguinte fórmula: Salário * Alíquota - Dedução
Ou seja, o trabalhador que ganha até 1903,98 não paga IRPF.
O que tem por base de cálculo de 2000 paga: 2000*15%-142,80 = 157,20


Nesse dojo, a base de cálculo será considerada o salário bruto - desconto do INSS.

Quem tem por salário bruto 3.000 reais terá:

Desconto de INSS: 12% -> 360
Base de cálculo para IPRF = 3.000 - 360 = 2640
Alíquota: 7,5%, dedução: 142,80
Desconto de IRPF = 2640 * 7,5% - 142,80 = 55,20
Salário líquido = 3000 - 360 - 55,20 = 2584,8


Obs.: Lembre-se que as alíquotas podem mudar anualmente, e em alguns anos mudam mais de uma vez no mesmo ano. Pense em deixar o seu código o mais apropriado possível para quem precisar usá-lo/alterá-lo posteriormente.


## Participantes

- James Peres
- Claudio Berrondo
- Daniel Drumond
- Helder Doutel
- Kaique 
- Bruno Osório
- Júlio Marins


## Retrospectiva

### 😀

- 8x8!
- presença irreverente do nosso grande camarada James Peres
- Bruno feliz com o problema! (ele fez novos clientes)
- muitos participantes participativos (para o Stream Yard!!)
- Python de novo
- novatos!

### 😩

- Marina não participou!!!
- jitsi
- Stream Yard
- James sumiu antes da hora (não vai ter pos dojo com o James, dojo terapia)
- reforma tributária já!
- Python de novo
- Não teve paçoca

### 🤫

- Python de novo
- Pensar em manter repl.it pro? 8x8?

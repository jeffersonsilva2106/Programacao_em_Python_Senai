print('hotel n sei oq')

idade = 29
cadastro = 'lala'

cadastro =  input('Digite o cadastro')
idade = int(input('Digite a sua idade'))

if cadastro == cadastro and idade == idade:

 idade = 34
cadastro = 'maria'

cadastro =  input('Digite o cadastro')
idade  = int(input('Digite a sua idade'))

if cadastro == cadastro and idade == idade:

 idade = 12
cadastro = 'gu'
cadastro =  input('Digite o cadastro')
senha  = int(input('Digite a sua idade'))

opçoes = ['simples', 'duplo', 'luxuoso']
reserva = []
total = []

valores = [100, 150, 250]
print(opçoes)

escolha  =  input('Deseja fazer o pedido? sim/não')
if escolha == 'sim':
        opçao0 = int(input('>'))


        opçao1 = int(input('>'))


        opçao2 = int(input('>'))

        
reserva += (opçoes[opçao0],opçoes[opçao1],opçoes[opçao2])
total +=(valores[opçao0],valores[opçao1], valores[opçao2])
print('reserva:', total)

soma = sum(total)


print(f'R$, {soma:.2f}')
print(f'''

print('qual a forma de pagamento?')
    1 - PIX
    2 - CC
    3 - CD  
    ''')
forma_pag =  input('Digite a forma de pagamento')
  
if forma_pag:
            print('obrigado, volte sempre')  
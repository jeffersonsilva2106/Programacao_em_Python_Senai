
# # mul = int((input
# # for numero in range (11):
# #     calculo = numero * mul 
# # print(mul, 'x', numero, '=' calculo)

# # csrrinho + []
# # for n in range(3):
# # produto = input('produto')

# while True:
#     print('infinito')

ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },

        'roupas':{
            'camiseta':150.0,
            'calça':250.0

        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }


}



carrinho = []
valores = [] #criar a lista de valores
deseja = input('deseja comprar? sim / nao?')
while deseja == 'sim':
    secao = input('secao - celulares roupas ou acessorios')
    p1 = input(f'Produto: {secao}')
    carrinho.append(p1)
    valores.append(ecommerce[secao][p1])
    print(carrinho)
    total + sum(valores)
    ptint('R$', total)
    deseja = input('Deseja continuar? sim / nao?')
else:
    print('Obrigada volte sempre!')   
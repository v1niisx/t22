#Validador de Triangulo

print('\n\t\t --- Validador de Triangulo --- \n\t\t')

#Entradas

la = float(input('Digite o Valor do Lado A:\n').strip())
lb = float(input('Digite o Valor do Lado B:\n').strip())
lc = float(input('Digite o Valor do Lado C:\n').strip())

#Processamento e Saida

lp = la < (lb+lc) and lb < (la+lc) and lc < (la + lb)

if lp == True:
    print('É um Triangulo Válido!')
    if la == lb and la == lc:
        print('Este triangulo é Equilátero!')
    elif la and lb == la:
        print('Este triangulo é Isósceles')
    else:
        print('Este triangulo é Escaleno')
else:
    print('Não é um Triangulo válido')


#Validar Triangulo
print('\n\t\t --- Validador de Triangulo --- \n\t\t')
#Entradas
la = float(input('Digite o Valor do Lado A: ').strip())
lb = float(input('Digite o Valor do Lado B: ').strip())
lc = float(input('Digite o Valor do Lado C: ').strip())
#Processamento e Saida
lp = la < (lb+lc) and lb < (la+lc) and lc < (la + lb)

if lp == True:
    print('É um Triangulo Válido!')

else:
    print('Não é um Triangulo válido')

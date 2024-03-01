print('----------- CALCALADORA -----------')
print('            BEM VINDO(a)'           )
print('-----------------------------------')
print('                                   ')

while True:
    print('                                   ')
    print('------------ OPERAÇÕES ------------')
    print('             OPÇÕES                ')
    print('             1 - Soma (+)          ')
    print('             2 - Subtração (-)     ')
    print('             3 - Multiplicação (*) ')
    print('             4 - Divisão (/)       ')
    print('             5 - Potencia (**)     ')
    print('             6 - tabuada           ')
    print('             7 - Sair              ')
    print('-----------------------------------')
    print('                                   ')

    opcao = int(input('escolha uma opção: '))

    if opcao == 1:
        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))
        resultado = numero1 + numero2
        print(f'{numero1} + {numero2} = {resultado}')

    elif opcao == 2:
        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))
        resultado = numero1 - numero2
        print(f'{numero1} - {numero2} = {resultado}')

    elif opcao == 3:
        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))
        resultado = numero1 * numero2
        print(f'{numero1} X {numero2} = {resultado}')

    elif opcao == 4:
        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))
        resultado = numero1 / numero2
        print(f'{numero1} / {numero2} = {resultado}')

    elif opcao == 5:
        numero1 = float(input('digite o primeiro numero: '))
        numero2 = float(input('digite o segundo numero: '))
        resultado = numero1 ** numero2
        print(resultado)

    elif opcao == 6:
        numero = int(input('digite um numero inteiro: '))

        contador = 1
        print(f'tabuada de: {numero}')
        while contador <= 10:
            resultado = numero * contador
            print('')

    elif opcao == 7:
        print('                                   ')
        print('----------- Já vai? :( ------------')
        print('----------- até a proxima ---------')
        break

    
    print('                                   ')
    print('----------- continuar? ------------')
    print('            sim ou nao?            ')
    print('-----------------------------------')
    print('                                   ')
    continuar = input('s / n: ')
    if continuar != 's' and continuar != 'S':
        print('                                   ')
        print('----------- Já vai? :( ------------')
        print('----------- até a proxima ---------')
        break
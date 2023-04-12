
while True:
    try:
        num = float(input('Digite um numero => '))
        if num % 2 == 0:
            print('numero Par')
            
        else:
            num % 2 != 0
            print('Este Numero é Impar')    
        break
    except ValueError:
        print('Entrada invalida. Porfavor, digite um numero')

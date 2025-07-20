#alt c o   mi comando para activar-desactivar copilot 
numeros = [122, 24, 3, 423, 52, 62, 33311, 73, 8, 9, 10, 11, 12, 13, 14, 15]

def max_num(numeros):
    numeroMaximo = 0
    for num in numeros:
        if num > numeroMaximo:
            numeroMaximo = num
    print(numeroMaximo)

max_num(numeros)

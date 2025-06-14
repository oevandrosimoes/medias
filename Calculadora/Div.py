from VerificarZero import verificarZero
def div(num1, num2):
    if verificarZero(num2):
        div = 'Divisão por zero é impossível'
    else:
        div = num1/num2
    return div
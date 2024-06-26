def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Simbolo ser um caracter unico')

    if width <= 2:
        raise Exception('Largura deve ser maior que 2')

    if height <= 2:
        raise Exception('Altura deve ser maior que 2')

    print(symbol*width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2) ) + symbol)
    print(symbol*width)

for sym, w, h in (('*',4,4),('0',20,5),('x',1,3),('ZZ',3,3)):
    try:
        boxPrint(sym,w,h)
    except Exception as err:
        print('Uma exceção foi encontrada:' + str(err))


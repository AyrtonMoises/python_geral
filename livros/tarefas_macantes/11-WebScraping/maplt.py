
#inicia um mapa no navegador usando um endereco da linha de comando ou do clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Pega endereço da linha de comando
    address = ' '.join(sys.argv[1:])
else:
    # Pega endereço do clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

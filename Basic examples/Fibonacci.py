llistaAuria = []
def auria(numero):
    primer = 0
    segon = 1
    for i in range(numero):
        tercer = segon+primer
        primer = segon
        segon = tercer

        llistaAuria.append(primer)

    print(llistaAuria)

def auria2(numero, rang1):
    primer = 0
    segon = 1
    for i in range(numero):
        tercer = segon+primer
        primer = segon
        segon = tercer

        llistaAuria.append(primer)

    print(llistaAuria[rang1:numero])

def numeroITipus():
    numero = int(input("Número desitjat: "))
    tipo = int(input("Com vols imprimir-ho? Tots[1] o Entre un rang[2]"))
    if tipo == 2:
        rang1 = int(input("Número inicial (El número final del rang es el numero anteriorment introduït)"))
        auria2(numero, rang1)
    elif tipo == 1:
        auria(numero)
    else:
        print("No vàlid.")

numeroITipus()



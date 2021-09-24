def tarjetas(a,b):
    plumones= (b*35)
    pliegos= (a*12)
    if pliegos<plumones:
        return(pliegos)
    elif plumones<pliegos:
        return(plumones)
def main():
    pliegos= int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones= int(input('Dame la cantidad de plumones: '))
    salida= tarjetas(pliegos,plumones)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(salida))
    

if __name__=='__main__':
    main()

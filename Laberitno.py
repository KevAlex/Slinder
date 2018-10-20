def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][:-2]
##    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")
def cargar_inicio(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][-2][0].split(",")

def cargar_fin(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][-1][0].split(",")


def arriba(lab, fil,col):
##    muevo solo en fila y muevo tanto para der como izq
    print 'fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
        print list(x)[col], 'arriba'
        if list(x)[col]== '0':
            print 'si'
            arriba(lab,[int(cargar_inicio(lab)[0])-2][0], int(cargar_inicio(lab)[1]))
##            arriba(lab, (fil-1),col)
        else:
            print 'cambia camino'
            izq(lab,(fil+1), (col-1))
            
                
##def der(lab):
##    print 'me muevo en col der'
##    arriba(lab, fil,col)
##    izq()
##    abajo()
##    
def izq(lab, fil, col):
##    print 'me muevo en col izq'
    print 'fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
        if list(x)[col]== '0':
            izq(lab,(fil), (col-1))
        print list(x)[col], 'fin'
        else:
            abajo(lab, fil, (col+1))
##    der(l)
##    abajo()
            
def abajo(lab, fil, col):
    print 'ss'
    
    
##    der()
    
def resolver(lab):
##    print "laberinto : ", cargar_archivo(lab)
    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","), 'fila'
    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])-1][0].split(","), 'fila-1'
    
    for x in cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","):
        print list(x)[int(cargar_inicio(lab)[1])], 'valor'
        
    arriba(lab, [int(cargar_inicio(lab)[0])-1][0], int(cargar_inicio(lab)[1]))
##    der(lab)
##    izq(lab)
##    abajo(lab)
            

               
    print "inicio : "
    print cargar_inicio(lab)
     
##    print "fin : "
##    print cargar_fin(lab)
    
resolver("labe.txt")

    


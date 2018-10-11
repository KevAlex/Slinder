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
        print list(x)[col]
        

def der():
    print 'me muevo en col der'
    arriba(lab, fil,col)
    izq()
    abajo()
    
def izq():
    print 'me muevo en col izq'
    arriba(lab, fil,col)
    der()
    abajo()
    

def abajo():
    print 'ss'
    arriba(lab, fil,col)
    izq()
    der()
    
    
    
def resolver(lab):
##    print "laberinto : ", cargar_archivo(lab)
    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","), 'fila'
    
    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])-1][0].split(","), 'fila+'
    
    for x in cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","):
        print list(x)[int(cargar_inicio(lab)[1])], 'col'
    arriba(lab, [int(cargar_inicio(lab)[0])-1][0], int(cargar_inicio(lab)[1]))
    der()
    izq()
    abajo()
            

               
    print "inicio : "
    print cargar_inicio(lab)
     
##    print "fin : "
##    print cargar_fin(lab)
    
resolver("labe.txt")

    


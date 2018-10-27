def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][:-2]
##    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")
def cargar_inicio(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][-2][0].split(",")

def cargar_fin(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][-1][0].split(",")


def arriba(lab, fil,col):
##    muevo solo en fila y muevo tanto para der como izq
##    print 'MOV Arriba','fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
##        print list(x)[col], 'for arriba'
        if list(x)[col]== '0':
            if (fil == int(cargar_fin(lab)[0]) and col == int(cargar_fin(lab)[1])):
                print '***********Si existe camino'
                
            arriba(lab,(fil-1), col)
##            print 'REC arriba', 'FIL', fil, 'COL', col
            izq(lab, fil, (col-1))
            der(lab,fil, (col+1))
##        else:
##            print 'Sale arriba', list(x)[col]

def abajo(lab, fil, col):
##    print 'MOV Abajo','fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
##        print list(x)[col], 'for abajo'
        if list(x)[col]== '0':
##            print 'hola'
##            abajo(lab,[int(cargar_inicio(lab)[0])+1][0], int(cargar_inicio(lab)[1]))
            if (fil == int(cargar_fin(lab)[0]) and col == int(cargar_fin(lab)[1])):
                print '***********Si existe camino'
                
            abajo(lab, (fil+1), col)
##            print 'REC abajo','FIL', fil, 'COL', col
            der(lab, fil, (col+1))
            izq(lab,fil, (col-1))
##        else:
##            print 'Sale abajo', list(x)[col]
            
            
def der(lab, fil, col):
##    print 'MOV derecha', 'fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
##        print list(x)[col], 'for derecha'
        if list(x)[col] == '0':
            if (fil == int(cargar_fin(lab)[0]) and col == int(cargar_fin(lab)[1])):
                print '***********Si existe camino'
                
            der(lab, fil, (col+1))
##            print 'REC derecha', 'FIL', fil, 'COL', col
            arriba(lab, (fil-1), col)
            abajo(lab, (fil+1), col)
            
##        else:
##            print 'Sale der', list(x)[col]
  
def izq(lab, fil, col):
##    print 'MOV izq','fila',fil,'colum',col
    for x in cargar_archivo(lab)[fil]:
##        print list(x)[col], 'for izquierda' 
        if list(x)[col]== '0':
            if (fil == int(cargar_fin(lab)[0]) and col == int(cargar_fin(lab)[1])):
                print '***********Si existe camino'
                
            izq(lab,(fil), (col-1))
##            print 'REC izquierda', 'FIL', fil, 'COL', col
            arriba(lab,(fil-1), col)
            abajo(lab, (fil+1), col)
##        else:
##            print 'Sale izq', list(x)[col]
##          
            
 
    
def resolver(lab):
##    print "laberinto : ", cargar_archivo(lab)
##    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","), 'fila'
##    print cargar_archivo(lab)[int(cargar_inicio(lab)[0])+1][0].split(","), 'fila+1'
    
##    for x in cargar_archivo(lab)[int(cargar_inicio(lab)[0])][0].split(","):
##        print list(x)[int(cargar_inicio(lab)[1])], 'Pos Inicial'
        
    #arriba(lab, [int(cargar_inicio(lab)[0])-1][0], int(cargar_inicio(lab)[1]))
    abajo(lab, [int(cargar_inicio(lab)[0])+1][0], int(cargar_inicio(lab)[1]))
    arriba(lab,  [int(cargar_inicio(lab)[0])-1][0],  int(cargar_inicio(lab)[1]))
    der(lab, [int(cargar_inicio(lab)[0])][0],  (int(cargar_inicio(lab)[1])+1) )
    izq(lab, [int(cargar_inicio(lab)[0])][0], (int(cargar_inicio(lab)[1])-1))
    
          
    print "inicio : "
    print cargar_inicio(lab)
     
    print "fin : "
    print cargar_fin(lab)
    
    
resolver("labe.txt")

    


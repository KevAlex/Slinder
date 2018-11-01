# Solucion Laberinto

## Integrantes:
  * Brayan Castañeda
  * Kevin Alexander Diaz
  * Sebastian Duque Gallego    20162020039
  
#### Introduccion:

El proposito de este proyecto es recibir un laberinto(los 0 son camino disponible y los 1 son paredes) y coordenadas de inicio(Punto donde iniciara a recorrerse el laberinto) y una coordenada de finalizar(Salida del laberinto).

#### Funciones:

 * cargar_archivo: Esta funcion recibira un archivo de texto y retornara primero todo el contenido menos las 2 ultimas lineas,luego la penultima linea y posteriormente la ultima linea del archivo de texto.
 
 * cargar_inicio: Esta funcion recibira un archivo de texto y retornara la penultima linea de dicho archivo.
 
 * cargar_fin: Esta funcion recibira un archivo de texto y retornara la ultima linea de dicho archivo.
 
 * arriba: Esta funcion recibira una archivo de texto y dos numeros el primero sera la fila y el segundo la columna,Compara la posicion en la que se encuentra y si es un 0 pasara a comprobar la posicion actual con la posicion de cargar_fin y si es la misma se imprimira que el laberinto tiene solucion, si no llamara a la funcion arriba quitandole uno a la fila y luego llamar a las funciones derecha e izquierDa.
 
 * abajo: Esta funcion recibira una archivo de texto y dos numeros el primero sera la fila y el segundo la columna,Compara la posicion en la que se encuentra y si es un 0 pasara a comprobar la posicion actual con la posicion de cargar_fin y si es la misma se imprimira que el laberinto tiene solucion, si no llamara a la funcion abajo sumandole uno a la fila y luego llamar a las funciones derecha e izquierda.
 
 * der: Esta funcion recibira una archivo de texto y dos numeros el primero sera la fila y el segundo la columna,Compara la posicion en la que se encuentra y si es un 0 pasara a comprobar la posicion actual con la posicion de cargar_fin y si es la misma se imprimira que el laberinto tiene solucion, si no llamara a la funcion dersumandole uno a la columna y luego llamar a las funciones arriba y abajo.+
 
  * izq: Esta funcion recibira una archivo de texto y dos numeros el primero sera la fila y el segundo la columna,Compara la posicion en la que se encuentra y si es un 0 pasara a comprobar la posicion actual con la posicion de cargar_fin y si es la misma se imprimira que el laberinto tiene solucion, si no llamara a la funcion izq restandole uno a la columna y luego llamar a las funciones arriba y abajo.
  
  * resolver: Esta funcion es la encarga de imprimir todos los pasos que se haran para llegar a la solucion del laberinto, en la cual llama a los 4 metodos arriba, abajo,der y izq
  
  
 

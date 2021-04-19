# Juego de la vida - Retroalimentacion NB (Python - processig 3)
# some ideas where extract from 'Game of Life' By Joan Soler-Adillon (Processing3+, Java)
# teoria del juego de la vida consultadas en: Wikipedia y de un informe del juego de la vida realizado por Manuel Romero Dopico. 

# Funciones para realizar las tareas descritas: 
# - patrones ingresados: para manualmente ingresar patrones se debe pausar el juego - con las teclas enter- y con el cursor seleccionar los espacios deseados
# con la doble seleccion deshacemos las seleccion hecha.
# - flujo del juego: para reanudar presionar enter, luego de una pausa realizada con la misma teclas.
# Para generar una matriz aleatoria presionar r o R, para establecer todos los valores de la matriz a cero presionar e o E

pause = False
copCells = []                                        # copCells corresponde a la copia de la matriz cells donde se guardan los valores (1 o 0), esto facilita   
cells = []                                           # manipular mas adelante las matrices para establecer los estados y la interaccion de las celulas.
cellSize = 20    
default = 15                                         # default: 'porcentaje' de celulas vivas (entre mas alto el numero ingresado mas probabilidad de que las casillas 
frame = 5                                            #  tomen valores de celulas vivas (1))

created = []

def setup():                                            
    size(800, 600)                                  # preferiblemente un valor fijo                             
    stroke('#989674')
    background(0)
    strokeWeight(1)
    noSmooth()
    frameRate(frame)                                # frameRate: establece la 'velocidad' de la evolucion del juego
    for i in range(width/cellSize):
        columna = []
        for j in range(height/cellSize):
            if random(100) < default:               # de manera aleatoria establecemos las celulas vivas y las muertas dada la variable default
                columna.append(1)
            else:
                columna.append(0)
        cells.append(columna)
        copCells.append (columna)

def draw():
    frameRate(frame)
    for i in range(width/cellSize):                     # dibujo de las condiciones iniciales de la matriz
        for j in range (height/cellSize):
            if cells[i][j] == 1:
                fill ('#BFD400')
            else:
                fill(0)
            rect(i*cellSize,j*cellSize,cellSize,cellSize)

        
    if ((mousePressed == True) and (pause == True)):    # manipular la matriz con el mouse mientras el juego esta en pausa.   (interaccion mouse)
        x_cell = int(map(mouseX, 0, width, 0, width/cellSize))  # (Game of Life By Joan Soler-Adillon (Processing3+, Java))
        # x_cell = constrain(x_cell, 0, width/cellSize)         # Nota: por el momento dada la 'funcion' map y otras pruebas realizadas con la 'funcion' map
        y_cell = int(map(mouseY, 0, height, 0, height/cellSize)) # se observo que los valores de rango en x_cell y y_cell dados en map() ya limitan los valores
        # y_cell = constrain(y_cell, 0, height/cellSize)         # por lo tanto resulta inecesario añadir constrain a la variable.

        if (copCells[x_cell][y_cell] == 1):             # seleccionamos manualmente celulas muertas
            cells[x_cell][y_cell] = 0 
        else:
            cells[x_cell][y_cell] = 1                   # seleccionamos manualmente celulas viva
            
    elif ((pause == True) and (mousePressed == False)): # guarda cambios introducidos con el cursor
        for i in range(width/cellSize):                 # (deep copy) realizamos una copia 'profunda' por columnas de las dos matrices creadas (para evitar 
            copCells[i] = list(cells[i])                # que los cambios en una alteren la otra y viceversa).
        
    if pause == False:                                  # condicion que permite el flujo del juego dada la variable pausa
        stroke('#989674')
        estados()
    
    fill(0)
    cout()
    
def cout():
    rect(0,0,400,40)
    textSize(20)
    if pause:
        fill(0,0,150)
        text("FrameRate = " + str(frame)+ " || % Default = " + str(default),20,25)
    else:
        fill('#BFD400')
        text("FrameRate = " + str(frame)+ " || % Default = " + str(default),20,25)
        
def estados(): # 'estados de las celulas'
    for i in range(width/cellSize):                     # 'deep copy' aseguramos la copia antes de empezar a cambiar los estados de las celulas
        copCells[i] = list(cells[i])
        
            
    for i in range(width/cellSize):
        for j in range(height/cellSize):
            neighbours = 0 
            for m in range(i-1,i+2):                     # rango establecido para verificar vecinos en las columnas
                for n in range(j-1,j+2):                 # rango establecido para verificar vecinos en las filas
                    
                    if ((m>=0) and (m<(width/cellSize))):
                        if ((n>=0) and (n<(height/cellSize))):
                            if (i,j) != (m,n):           # verifica que no se cuente a si mismo entre las combinaciones de m y n
                                if copCells[m][n] == 1:  # NOTA PERSONAL RELACIONADA CON UN PROBLEMA YA SOLUCIONADO.
                                    neighbours += 1      # NOTA RELACIONADA AL PROBLEMA PRESENTADO EN CLASE: el problema se puede deber a la manera en la que recorremos las matriz dado que se iniciaba desde 
            if copCells[i][j] == 1:                      # el origen y recorria las filas de manera horizontal y no vertical (RESUELTO)--> tecnicamente este si era un problema y se observo el cambio,
                if (neighbours<2) or (neighbours>3):     # sin embargo para algunas figuras no resulta (HIPOTESIS: presiento que hay algo anda mal con la copia de las matrices)
                    cells[i][j] = 0                      # la copia que estaba realizando era una copia superficial ('shallow copy') por lo tanto las matrices copCells y cells siempre iban a ser las mismas de tal
            else:                                        # forma que al iterar se revisaba el mismo cambio y no la original(matriz anterior) PROBLEMA YA RESUELTO.
                if neighbours == 3:
                    cells [i][j] = 1

def keyPressed(): # interaccion con el teclado
    global pause, frame, default
        
    if (key == ENTER):                     # pausa 
        pause = not(pause)
        stroke(0,0,120)
            
    if (key == 'E') or (key == 'e'):                     # restablecer los valores de la matriz a 0
        for i in range(width/cellSize): 
           for j in range(height/cellSize):
                copCells[i][j] = 0
                cells[i][j] = 0
                
    if (key == 'r') or (key == 'R'):                   # generar matriz aleatoria
       for i in range(width/cellSize):
        for j in range(height/cellSize):
            if random(100) < default:                  # de manera aleatoria establecemos las celulas vivas y las muertas dada la variable default
                cells[i][j] = 1
                copCells[i][j] = 1
            else:
                cells[i][j] = 0
                copCells[i][j] = 0
                
    if (key == CODED):                                 # FPS interaction
        if (keyCode == UP):
            frame += 1
        elif (keyCode == DOWN) and (frame != 1):       # limitamos el valor minimo de frame
            frame -= 1
        elif  (keyCode == LEFT) and (default != 5):    # solamente se ve el cambio cuando reiniciamos la matriz (cambiamos las probabilidad de que la celula este viva)
            default -= 5
        elif (keyCode == RIGHT) and (default <= 95):
            default += 5
        elif (keyCode == SHIFT):                       # volvemos a las condiciones de frame y default iniciales 
            frame = 5
            default = 15

    if (key == 'd') or (key == 'D'):
        created.append(cells)


                

        
        

        

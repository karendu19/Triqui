import pygame
import time
#crear un motor
pygame.init()

#definir las dimenciones que va tenerla ventana de juego
screen= pygame.display.set_mode((450,450))
#pygame.displayset_caption("juego triki")
pygame.display.set_caption("juego triki")
#cargar las imagenes
fondo=pygame.image.load("img/Tablero.png")
circulo=pygame.image.load("img/Circulo.png")
equis=pygame.image.load("img/Equis.png")
reseteado=pygame.image.load("img/reseteado.png")
ganoO=pygame.image.load("img/ganoO.png")
ganoX=pygame.image.load("img/ganoX.png")

# Renderizamos imagenes
fondo=pygame.transform.scale(fondo,(450,450))
circulo=pygame.transform.scale(circulo,(125,125))
equis=pygame.transform.scale(equis,(110,100))
reseteado=pygame.transform.scale(reseteado,(50,30))
ganoO=pygame.transform.scale(ganoO,(100,50))
ganoX=pygame.transform.scale(ganoX,(100,50))
# creamos matrices de guia
coordenadas=[[(40,55),(160,55),(275,55)], 
            [(40,170),(160,170),(275,170)],
            [(40,285),(160,285),(275,285)]]

tablero=[["","",""], 
            ["","",""],
            ["","",""] ]  

#variables de control
 #para saber quien tiene turno
listadoX=[0,1,2]
triqui=False

turno="O"
# cuando termine
game_over=False
# para     
reloj=pygame.time.Clock()

#establecer la logica del juego
def graficartablero(triqui, turno):
    # mostramos el fondo o llenamos la ventana con la imagen
    screen.blit(fondo,(0,0))
    screen.blit(reseteado, (199,420))
    
    
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna]=="O":
                graficar_O(fila,columna)
            elif tablero[fila][columna]=="X":
                graficar_X(fila,columna)

    if triqui:
        if turno=="X":
           screen.blit(ganoO,(0,0))
        elif turno=="O":
            screen.blit(ganoX,(0,0))
        

                                 
    pygame.display.flip() 
              
# funcion para graficar la X o la O
def graficar_O(fila, columna):
    screen.blit(circulo,coordenadas[fila][columna])

def graficar_X(fila, columna):
    screen.blit(equis,coordenadas[fila][columna])  
     
def graficar_reseteado(tablero):
    tablero=[["","",""], 
           ["","",""],
           ["","",""]]
    return tablero     

# iniciar el juego
contadorX=0
contadorO=0
while not game_over:
    reloj.tick(30)

    for evento in pygame.event.get():
        # definimos cuando se cierra el juego con boton cerrar
        if evento.type==pygame.QUIT:
            game_over=True
        elif evento.type==pygame.MOUSEBUTTONDOWN:
            
            mouseX,mouseY=evento.pos
            if triqui == False:
                if(mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                    fila=(mouseY-50)//125
                    columna=(mouseX-40)//125
                    if tablero[fila][columna]=="":
                        tablero[fila][columna]=turno
                        for a in listadoX:
                            if turno == tablero[0][a] and turno == tablero[1][a] and turno == tablero[2][a]:
                                triqui=True
                                
                            elif turno == tablero[a][0] and turno == tablero[a][1] and turno == tablero[a][2]:
                                triqui=True
                                
                            elif turno == tablero[0][0] and turno == tablero[1][1] and turno == tablero[2][2]:
                                triqui=True
                                
                            elif turno == tablero[0][2] and turno == tablero[1][1] and turno == tablero[2][0]:
                                triqui=True    
                        
                                
                        graficartablero(triqui, turno)
                        contador=0
                        for i  in tablero:
                            if "" not in i:
                               contador=contador + 1
                        if contador==3:
                            pygame.display.set_caption("Empate")         
                            
                        if triqui:
                            pygame.display.set_caption(f"¡{turno} ha ganado!")
                            if turno=="O":
                                contadorO= contadorO+1
                                print("Ha ganado", turno, "y lleva",contadorO,"victorias") 
                                
                            elif turno=="X":
                                contadorX = contadorX+1
                                print("Ha ganado", turno, "y lleva",contadorX,"victorias")  
                                
                        if turno=="O":
                            turno="X"
                        else:
                           turno="O"
            if(mouseX>=199 and mouseX < 249) and (mouseY > 420 and mouseY < 450):
                turno="O"
                triqui=False
                tablero=graficar_reseteado(tablero)
                graficartablero(triqui, turno)
                              
                
    graficartablero(triqui, turno) #199,400
    
    

# si esta lleno el tablero finaliza
pygame.quit        
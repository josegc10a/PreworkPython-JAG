



def crear_tablero():
    tablero = [[" " for iterador in range (3)] for iterador in range (3)]
    return tablero

def imprimir_tablero(tablero):
    print("-" * 9)
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def is_tablero_lleno(tablero):
    return all(all(casilla !=" " for casilla in fila) for fila in tablero)

def comprobar_ganador(tablero, jugador):
    for i in range(3):
            if all(tablero [i][j] == jugador for j in range(3)) or all(tablero [j][i] == jugador for j in range(3)):
                return True
          
            if all(tablero [i][j] == jugador for j in range(3)) or all(tablero [i][2-i] == jugador for j in range(3)):
                return True
    return False


def tres_en_linea():
    tablero=crear_tablero()
    jugador_actual = 'X'


    print('Bienvenido/a!! Estais jugando al tres en linea')
    imprimir_tablero(tablero)
    while True:
        
        print(f"Turno de jugador {jugador_actual}")
        fila= int(input("Elige Fila 0, 1, 2: "))
        columna = int(input("Elige Columna 0, 1, 2: "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if comprobar_ganador (tablero,jugador_actual):
                print(f'El jugador {jugador_actual} ha ganado!')
                break
            if is_tablero_lleno(tablero):
                print('EMPATE!!')
                break

            jugador_actual ='O' if jugador_actual =='X' else 'X'
            #if jugador_actual == 'X':
            #    jugador_actual= 'O'
            #else: 
            #    jugador_actual = 'X'

        else:
            print('casilla ocupada')



if __name__ == "__main__":
    tres_en_linea()
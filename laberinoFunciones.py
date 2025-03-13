FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def crear_laberinto():
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    return laberinto

def mostrar_laberinto(laberinto, fila_jugador, columna_jugador):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end="")  # Jugador
            elif laberinto[i][j]:
                print("O ", end="")  # Meta
            else:
                print(". ", end="")  # Espacio vacío
        print()

def mover_jugador(fila_jugador, columna_jugador, movimiento):
    if movimiento == 'i' and fila_jugador > 0:
        return fila_jugador - 1, columna_jugador
    elif movimiento == 'k' and fila_jugador < FILAS - 1:
        return fila_jugador + 1, columna_jugador
    elif movimiento == 'j' and columna_jugador > 0:
        return fila_jugador, columna_jugador - 1
    elif movimiento == 'l' and columna_jugador < COLUMNAS - 1:
        return fila_jugador, columna_jugador + 1
    else:
        print("Movimiento no válido.")
        return fila_jugador, columna_jugador

def main():
    laberinto = crear_laberinto()
    fila_jugador, columna_jugador = 0, 0
    
    while True:
        mostrar_laberinto(laberinto, fila_jugador, columna_jugador)
        
        if (fila_jugador, columna_jugador) == (META_FILA, META_COLUMNA):
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break
        
        movimiento = input("\nIngrese movimiento (w: arriba, s: abajo, a: izq, d: der): ")
        fila_jugador, columna_jugador = mover_jugador(fila_jugador, columna_jugador, movimiento)

if __name__ == "__main__":
    main()

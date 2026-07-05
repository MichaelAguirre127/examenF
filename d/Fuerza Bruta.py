def fuerza_bruta(monedas, i, j):



  if i == j:

    return monedas[i]



  if i + 1 == j:

    return max(monedas[i], monedas[j])



  tomar_izq = monedas[i] + min(

    fuerza_bruta(monedas, i + 2, j),

    fuerza_bruta(monedas, i + 1, j - 1)

  )



  tomar_der = monedas[j] + min(

    fuerza_bruta(monedas, i + 1, j - 1),

    fuerza_bruta(monedas, i, j - 2)

  )



  return max(tomar_izq, tomar_der)





def simulacion(monedas):

  turno = 1



  while monedas:



    if monedas[0] >= monedas[-1]:

      moneda = monedas.pop(0)

    else:

      moneda = monedas.pop()



    print(f"Turno del Jugador {turno}: tomó la moneda {moneda}")



    turno = 2 if turno == 1 else 1





def main():


  print("    JUEGO DE MONEDAS")

  monedas = list(map(int, input("Ingrese las monedas: ").split()))



  resultado = fuerza_bruta(monedas, 0, len(monedas) - 1)



  print("\nSimulación del juego")

  simulacion(monedas.copy())



  jugador2 = sum(monedas) - resultado



  print("\nRESULTADO")

  print(f"Puntaje Jugador 1: {resultado}")

  print(f"Puntaje Jugador 2: {jugador2}")



  if resultado > jugador2:

    print("\n GANADOR: Jugador 1")

  elif jugador2 > resultado:

    print("\n  GANADOR: Jugador 2")

  else:

    print("\n  EMPATE")



  print("\nJuego terminado")





if __name__ == "__main__":

  main()
def programaciondinamica(monedas):



  n = len(monedas)



  dp = [[0 for _ in range(n)] for _ in range(n)]



  for gap in range(n):

    for i in range(n - gap):



      j = i + gap



      x = dp[i + 2][j] if i + 2 <= j else 0

      y = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0

      z = dp[i][j - 2] if i <= j - 2 else 0



      dp[i][j] = max(

        monedas[i] + min(x, y),

        monedas[j] + min(y, z)

      )



  return dp[0][n - 1]





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

  monedas = list(map(int, input("Ingrese los valores de las monedas: ").split()))



  resultado = programaciondinamica(monedas)



  print("\nSimulación del juego")

  simulacion(monedas.copy())



  total = sum(monedas)

  jugador2 = total - resultado



  print("\nRESULTADO")

  print(f"Puntaje Jugador 1: {resultado}")

  print(f"Puntaje Jugador 2: {jugador2}")



  if resultado > jugador2:

    print("\n  GANADOR: Jugador 1")

  elif jugador2 > resultado:

    print("\n  GANADOR: Jugador 2")

  else:

    print("\n  EMPATE")



  print("\nJuego terminado")





if __name__ == "__main__":

  main()
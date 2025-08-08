import random
peticion = int(input("Quieres jugar un juego super cool? 1 = Siii!!, 2 = No: "))

if peticion == 1:
    print("Bienvenidos todos a este increiblemente tedioso juego de adivinar numeros! \n")
    print("Estoy pensando en un número aleatorio. \n")
    print("Tienes una cantidad selecta de chances para adivinar el número correcto. \n")
    print("Por favor selecciona el nivel de dificultad:")
    print("1. Fácil (10 chances)")
    print("2. Medio (5 chances)")
    print("3. Difícil (3 chances)")

    eleccion = int(input("Ingresa tu nivel de dificultad: "))
    # Dif. Facil
    if eleccion == 1:
        print("¡Bien! Elegiste la dificultad: Fácil")
        print("Empezemos el juego!!")
        numero1 = random.randint(0, 30)
        num_intentos = 10
        int_usados = 0
        while num_intentos > 0:
            facil = int(input("Ingresa tu número: "))
            if facil == numero1:
                print(f"¡Enhorabuena! ¡Elegiste el número correcto! Lo hiciste en {int_usados} intento(s).")
                break
            if facil < numero1:
                print(f"¡Noo! El número es mayor que {facil}")
            if facil > numero1:
                print(f"¡Noo! El número es menor que {facil}")
            num_intentos -= 1
            int_usados += 1
            print(f"Te quedan {num_intentos} intentos. \n")
            if num_intentos == 5:
                pista = int(input("Quieres una pista? 1- Si, 2- No: "))
                if pista == 1:
                    print("El rango de numeros es de 0 a 30.")
                elif pista == 2:
                    print("Oh, okey! Sigue jugando :)")
        if num_intentos == 0:
            print(f"Awhh, no pudiste adivinar el numero. Era {numero1}.")

    # Dif. Medio
    if eleccion == 2:
        print("¡Okey! Elegiste la dificultad: Medio")
        print("Empezemos el juego!!")
        numero2 = random.randint(0, 20)
        num_intentos2 = 5
        int_usados2 = 0
        while num_intentos2 > 0:
            medio = int(input("Ingresa tu número: "))
            if medio == numero2:
                print(f"¡Enhorabuena! ¡Elegiste el número correcto! Lo hiciste en: {int_usados2} intentos.")
                break
            if medio < numero2:
                print(f"¡Noo! El número es mayor que {medio}")
            if medio > numero2:
                print(f"¡Noo! El número es menor que {medio}")
            num_intentos2 -= 1
            int_usados2 += 1
            print(f"Te quedan {num_intentos2} intentos. \n")
            if num_intentos2 == 2:
                pista = int(input("¿Quieres una pista? 1 - Sí, 2 - No: "))
                if pista == 1:
                    print("El rango de números es de 10 a 20.")
                else:
                    print("Oh, okey! Sigue jugando :)")
            if num_intentos2 == 0:
             print(f"Awhh, no pudiste adivinar el numero. Era {numero2}.")

    # Dif. Dificil
    if eleccion == 3:
        print("¡Uf! Elegiste la dificultad: Difícil")
        print("Empezemos el juego!!")
        numero3 = random.randint(0, 10)
        num_intentos3 = 3
        int_usados3 = 0
        while num_intentos3 > 0:
            dificil = int(input("Ingresa tu número: "))
            if dificil == numero3:
                print(f"¡Enhorabuena! ¡Elegiste el número correcto! Lo hiciste en {int_usados3} intentos.")
                break
            if dificil < numero3:
                print(f"¡Noo! El número es mayor que {dificil}")
            if dificil > numero3:
                print(f"¡Noo! El número es menor que {dificil}")
            num_intentos3 -= 1
            int_usados3 += 1
            print(f"Te quedan {num_intentos3} intentos. \n")
            if num_intentos3 == 1:
                pista = int(input("¿Quieres una pista? 1 - Sí, 2 - No: "))
                if pista == 1:
                   print("El rango de números es de 10 a 20.")
                else:
                   print("Oh, okey! Sigue jugando :)")

        if num_intentos3 == 0:
            print(f"Awhh, no pudiste adivinar el numero. Era {numero3}.")

else:
    print("¡Está bien! Tal vez en otra ocasión :)")

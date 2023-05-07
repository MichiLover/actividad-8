from claseConjunto import Conjunto

if __name__ == '__main__':
    conjunto_a = Conjunto([1, 2, 3, 4])
    conjunto_b = Conjunto([3, 6, 9])

    opcion = 0
    while opcion != 4:
        print("1. Unión de conjuntos")
        print("2. Diferencia de conjuntos")
        print("3. Verificar igualdad de conjuntos")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
                conjunto_c = conjunto_a + conjunto_b
                print("A + B = {}".format(conjunto_c.elementos))
        elif opcion == 2:
                conjunto_d = conjunto_a - conjunto_b
                print("A - B = {}".format(conjunto_d.elementos))
        elif opcion == 3:
            if conjunto_a == conjunto_b:
                print("Los conjuntos son iguales")
            else:
                print("Los conjuntos son diferentes")
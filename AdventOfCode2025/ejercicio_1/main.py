from io import TextIOWrapper

def main() -> None:
    file: TextIOWrapper
    total_zeros : int = 0
    pasos_a_mover : int
    posicion : int = 50
    flag : int

    with open('input', 'r') as file:
        for line in file:
            flag = -1 if line[0].lower() == 'l' else 1 if line[0].lower() == 'r' else None
            pasos_a_mover = int(line[1:])
            # Calculamos vueltas completas, suamos 1 por cada una.
            total_zeros += pasos_a_mover // 100
            # Calculamos movimientos restantes por hacer tras calcular vueltas completas.
            movimientos_restantes = pasos_a_mover % 100
            # Por cada movimiento restante, calculamos la posición y comprobamos si es 0
            for i in range(movimientos_restantes):
                posicion = (posicion + flag) % 100
                if posicion == 0:
                    total_zeros += 1
    print(f"total de ceros: {total_zeros}")

if __name__ == "__main__":
    main()
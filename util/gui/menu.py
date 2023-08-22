
from dataclasses import dataclass


@dataclass
class Menu:

    _resultado: int = 0
    _informe: int = 0

    @property
    def resultado(self):
        return self._resultado

    @property
    def informe(self):
        return self._informe

    def showMenu(self):
        print("*" * 60)
        print("\n1. Extraer ofertas")
        print("\n2. Mostrar informes\n")
        print("*" * 60)
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            self._resultado = 1

        elif opcion == "2":
            self._resultado = 2

        return

    def showInformesMenu(self):
        print("\n" + "=" * 60 + "\n")

        print("*" * 60)
        print("\n1. Informe sobre los salarios medios en los puestos más populares.")
        print("\n2. Informe sobre ubicación y teletrabajo.")
        print("\n3. Informe sobre requisitos más demandados.")
        print("\n4. Informe sobre la experiencia y el numero de ofertas.")
        print("*" * 60)
        match input("Selecciona una opción: "):

            case "1":
                self._informe = 1

            case "2":
                self._informe = 2

            case "3":
                self._informe = 3

            case "4":
                self._informe = 4

        return

    def showExitMenu(self):
        print("\n" + "=" * 60 + "\n")
        print("*" * 60)
        print("\nSaliendo...\n")
        print("*" * 60)

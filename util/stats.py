from datetime import date
from os import getcwd, path


def imprime_stats():
    print("\n")
    print("=" * 60)
    print("\n")

    for portal in datos_portales:
        print("\n")
        print("*" * 60)
        print("\n")

        print(f"Datos de {portal['nombre']}:")

        print(
            f"Script bloqueado:........................{'Si' if portal['es_bloqueado'] else 'No'}"
        )
        if portal["es_bloqueado"]:
            print(
                f"Pantalla del captcha:....................{portal['ruta_captura_error']}"
            )
            print("\n")

        print(
            f"Total de ofertas analizadas:.............{portal['ofertas_analizadas']}"
        )
        print(
            f"Total de ofertas con salario:............{portal['ofertas_con_salario']}"
        )
        print(
            f"Total de ofertas con experiencia:........{portal['ofertas_con_experiencia']}"
        )
        print(
            f"Tiempo de recoleccion:...................{portal['tiempo_total']} mins."
        )

    print("\n")
    print("*" * 60)
    print("\n")

    print(f"Se han analizado {n_ofertas_analizadas} ofertas.")
    print(
        f"Solo {n_ofertas_con_salario} ofertas tienen informacion sobre el salario.")
    print(
        f"Solo {n_ofertas_con_experiencia} ofertas tienen informacion sobre la experiencia."
    )
    print(
        f"Tiempo para recoger los datos: {round((s_final - s_inicio) / 60, 2)} mins.")

    print("\n")
    print("=" * 60)


def exporta_stats():
    ruta = __obtener_ruta_archivo()

    with open(ruta, "w") as f:
        f.write("=" * 60)
        f.write("\n")

        for portal in datos_portales:
            f.write("\n")
            f.write("*" * 60)
            f.write("\n")

            f.write(f"Datos de {portal['nombre']}:\n")
            f.write("\n")
            f.write(
                f"Script bloqueado:........................{'Si' if portal['es_bloqueado'] else 'No'}\n"
            )
            if portal["es_bloqueado"] and portal["ruta_captura_error"] != "":
                f.write(
                    f"Pantalla del captcha:....................{portal['ruta_captura_error']}\n"
                )
                f.write("\n")

            f.write(
                f"Total de ofertas analizadas:.............{portal['ofertas_analizadas']}\n"
            )
            f.write(
                f"Total de ofertas con salario:............{portal['ofertas_con_salario']}\n"
            )
            f.write(
                f"Total de ofertas con experiencia:........{portal['ofertas_con_experiencia']}\n"
            )
            f.write(
                f"Tiempo de recoleccion:...................{portal['tiempo_total']} mins.\n"
            )

        f.write("\n")
        f.write("*" * 60)
        f.write("\n")

        f.write(f"Se han analizado {n_ofertas_analizadas} ofertas.\n")
        f.write(
            f"{n_ofertas_con_salario} ofertas tienen informacion sobre el salario.\n"
        )
        f.write(
            f"{n_ofertas_con_experiencia} ofertas tienen informacion sobre la experiencia.\n"
        )
        f.write(
            f"Tiempo para recoger los datos: {round((s_final - s_inicio) / 60, 2)} mins.\n"
        )

        f.write("=" * 60)


def __obtener_ruta_archivo():
    # Devuelve ruta de un csv con la fecha de hoy en el nombre
    fechaHoy = str(date.today())
    i = 0
    nombre_archivo = f"Estadisticas_ultima_ejecucion_{fechaHoy}_{str(i)}.txt"

    ruta = path.join(getcwd(), "data", "estadisticas", nombre_archivo)

    while path.exists(ruta):
        i += 1
        nombre_archivo = f"Estadisticas_ultima_ejecucion_{fechaHoy}_{str(i)}.txt"
        ruta = path.join(getcwd(), "data", "estadisticas", nombre_archivo)

    return ruta


n_ofertas_analizadas = 0
n_ofertas_con_salario = 0
n_ofertas_con_experiencia = 0

s_inicio = 0
s_final = 0

datos_portales: list[dict] = []

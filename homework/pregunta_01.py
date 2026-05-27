"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re
def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Eliminar la línea de guiones separadora
    text = re.sub(r"-{3,}\n", "", text)

    # Cada registro empieza con un número de cluster (línea con dígito al inicio)
    bloques = re.split(r"\n(?=\s*\d+\s+\d+)", text.strip())

    registros = []
    for bloque in bloques:
        # Unir líneas del bloque en una sola, colapsando espacios múltiples
        linea = " ".join(bloque.split())

        # Extraer los 4 campos
        match = re.match(
            r"(\d+)\s+(\d+)\s+([\d,]+\s*%)\s+(.+)", linea
        )
        if match:
            cluster        = int(match.group(1))
            cantidad       = int(match.group(2))
            porcentaje = float(match.group(3).replace(" ", "").replace(",", ".").replace("%", ""))
            palabras_clave = match.group(4).strip()

            # Normalizar palabras clave: separar por coma + un solo espacio
            palabras_clave = ", ".join(
                p.strip() for p in palabras_clave.split(",")
            ).rstrip(".")

            registros.append((cluster, cantidad, porcentaje, palabras_clave))

    df = pd.DataFrame(registros, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ])

    return df
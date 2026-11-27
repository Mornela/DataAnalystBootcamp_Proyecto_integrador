"""

BOOTCAMP DATA ANALYTICS • MÓDULO 0: FUNDAMENTOS DE PROGRAMACIÓN
Propuestas de Proyectos Integradores (Python Puro)
10 Retos Orientados a Negocio, Guías Funcionales y Datasets Simulados
Directrices de Trabajo para el Alumnado
Restricción técnica principal: Utiliza exclusivamente Python estándar (variables, listas, diccionarios,
condicionales, bucles y funciones). No uses librerías externas como pandas, numpy o re.
Modularidad exigida: Organiza tu solución en al menos 3 funciones independientes, con nombres
descriptivos, parámetros de entrada y return.
Control de versiones: Sube tu avance a un repositorio público en GitHub (desde VS Code o Google Colab)
mediante commits progresivos.
Entregable final: Archivo de código limpio (.py o .ipynb) + archivo README.md explicando el problema
de negocio, las métricas calculadas y tus principales hallazgos




PROYECTO 02
Analizador de Embudo de Conversión (Funnel Analytics)
OBJETIVO DE NEGOCIO
Nivel: Inicial
Descubrir en qué paso del proceso de compra online (visita → registro → carrito → compra) se están
perdiendo más clientes potenciales.
QUÉ DEBE HACER TU CÓDIGO (GUÍA DE TRABAJO)
Normalizar y deduplicar: Estandarizar el texto de las etapas y asegurarte de no contar dos veces a un
mismo usuario (user_id) si repitió una misma acción (por ejemplo, visitar la web dos veces).
Contabilizar por etapa: Agrupar cuántos usuarios únicos llegaron a cada una de las 4 etapas del embudo.
Detectar fugas: Calcular el porcentaje de usuarios que avanza de una etapa a la siguiente e identificar cuál
es el paso con mayor caída de conversión.
DATASET SIMULADO (PYTHON PURO)
eventos_web = [
{"user_id": "U01", "etapa": "visita", "dispositivo": "mobile"},
{"user_id": "U01", "etapa": "visita", "dispositivo": "mobile"},
{"user_id": "U01", "etapa": "registro", "dispositivo": "mobile"},
{"user_id": "U01", "etapa": "carrito", "dispositivo": "mobile"},
{"user_id": "U01", "etapa": "compra", "dispositivo": "mobile"},
{"user_id": "U02", "etapa": "Visita", "dispositivo": "desktop"},
{"user_id": "U02", "etapa": "registro", "dispositivo": "desktop"},
{"user_id": "U02", "etapa": "carrito", "dispositivo": "desktop"},
{"user_id": "U03", "etapa": "visita", "dispositivo": "mobile"},
{"user_id": "U03", "etapa": "registro", "dispositivo": "mobile"},
{"user_id": "U04", "etapa": "visita", "dispositivo": "desktop"},
{"user_id": "U05", "etapa": "visita", "dispositivo": "mobile"},
{"user_id": "U05", "etapa": "registro", "dispositivo": "mobile"},
{"user_id": "U05", "etapa": "carrito", "dispositivo": "mobile"},
{"user_id": "U05", "etapa": "compra", "dispositivo": "mobile"},
{"user_id": "U06", "etapa": "visita", "dispositivo": "tablet"}
]


"""



"""
Analizador de embudo de conversión.

Este programa usa únicamente Python estándar:
listas, diccionarios, conjuntos, bucles y funciones.
"""

eventos_web = [
    {"user_id": "U01", "etapa": "visita", "dispositivo": "mobile"},
    {"user_id": "U01", "etapa": "visita", "dispositivo": "mobile"},
    {"user_id": "U01", "etapa": "registro", "dispositivo": "mobile"},
    {"user_id": "U01", "etapa": "carrito", "dispositivo": "mobile"},
    {"user_id": "U01", "etapa": "compra", "dispositivo": "mobile"},
    {"user_id": "U02", "etapa": "Visita", "dispositivo": "desktop"},
    {"user_id": "U02", "etapa": "registro", "dispositivo": "desktop"},
    {"user_id": "U02", "etapa": "carrito", "dispositivo": "desktop"},
    {"user_id": "U03", "etapa": "visita", "dispositivo": "mobile"},
    {"user_id": "U03", "etapa": "registro", "dispositivo": "mobile"},
    {"user_id": "U04", "etapa": "visita", "dispositivo": "desktop"},
    {"user_id": "U05", "etapa": "visita", "dispositivo": "mobile"},
    {"user_id": "U05", "etapa": "registro", "dispositivo": "mobile"},
    {"user_id": "U05", "etapa": "carrito", "dispositivo": "mobile"},
    {"user_id": "U05", "etapa": "compra", "dispositivo": "mobile"},
    {"user_id": "U06", "etapa": "visita", "dispositivo": "tablet"}
]


def normalizar_y_deduplicar(eventos):
    """Convierte las etapas a minúsculas y elimina repeticiones por usuario y etapa."""
    eventos_unicos = set()

    for evento in eventos:
        user_id = evento["user_id"]
        etapa = evento["etapa"].strip().lower()
        eventos_unicos.add((user_id, etapa))

    return eventos_unicos


def contar_usuarios_por_etapa(eventos_unicos, etapas):
    """Devuelve un diccionario con los usuarios únicos de cada etapa."""
    usuarios_por_etapa = {}

    for etapa in etapas:
        usuarios = set()

        for user_id, etapa_evento in eventos_unicos:
            if etapa_evento == etapa:
                usuarios.add(user_id)

        usuarios_por_etapa[etapa] = len(usuarios)

    return usuarios_por_etapa


def calcular_conversiones(usuarios_por_etapa, etapas):
    """Calcula el avance entre etapas consecutivas."""
    conversiones = {}

    for posicion in range(len(etapas) - 1):
        etapa_actual = etapas[posicion]
        etapa_siguiente = etapas[posicion + 1]

        usuarios_actuales = usuarios_por_etapa[etapa_actual]
        usuarios_siguientes = usuarios_por_etapa[etapa_siguiente]

        if usuarios_actuales == 0:
            porcentaje = 0
        else:
            porcentaje = usuarios_siguientes / usuarios_actuales * 100

        nombre_conversion = etapa_actual + " -> " + etapa_siguiente
        conversiones[nombre_conversion] = round(porcentaje, 2)

    return conversiones


def identificar_mayor_caida(conversiones):
    """Identifica el o los pasos cuya conversión es más baja."""
    menor_conversion = min(conversiones.values())
    pasos_con_mayor_caida = []

    for paso, porcentaje in conversiones.items():
        if porcentaje == menor_conversion:
            pasos_con_mayor_caida.append(paso)

    return pasos_con_mayor_caida, round(100 - menor_conversion, 2)


def mostrar_resultados(usuarios_por_etapa, conversiones, mayor_caida, perdida):
    """Muestra los resultados de forma clara."""
    print("USUARIOS ÚNICOS POR ETAPA")
    for etapa, cantidad in usuarios_por_etapa.items():
        print(etapa.capitalize() + ": " + str(cantidad))

    print("\nCONVERSIÓN ENTRE ETAPAS")
    for paso, porcentaje in conversiones.items():
        print(paso + ": " + str(porcentaje) + "%")

    print("\nPASO O PASOS CON MAYOR CAÍDA")
    for paso in mayor_caida:
        print(paso + " - caida: " + str(perdida) + "%")


def main():
    etapas = ["visita", "registro", "carrito", "compra"]

    eventos_unicos = normalizar_y_deduplicar(eventos_web)
    usuarios_por_etapa = contar_usuarios_por_etapa(eventos_unicos, etapas)
    conversiones = calcular_conversiones(usuarios_por_etapa, etapas)
    mayor_caida, perdida = identificar_mayor_caida(conversiones)
    mostrar_resultados(usuarios_por_etapa, conversiones, mayor_caida, perdida)


main()

# PROBLEMA ACTUAL: Posible falso positivo en desplazamiento
import string
import random
import hashlib
import time
import os

# Variables globales
FRASE = "En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo de los de lanza en astillero adarga antigua rocin flaco y galgo corredor"
PALABRA_GUIA = ""
FRASE_CIFRADA = ""


def generar_semilla_caotica():
    # 1. Fuente: Hora actual en nanosegundos (muy volátil)
    fuente1 = str(time.perf_counter_ns()).encode('utf-8')

    # 2. Fuente: ID del Proceso (cambia con cada ejecución)
    fuente2 = str(os.getpid()).encode('utf-8')

    # 3. Fuente: Dirección de memoria de un nuevo objeto (volátil)
    fuente3 = str(id(object())).encode('utf-8')

    print("--- Mejorando Semilla (sin 'secrets') ---")
    print(f"Fuente 1 (Tiempo ns): {fuente1.decode()}")
    print(f"Fuente 2 (Process ID): {fuente2.decode()}")
    print(f"Fuente 3 (Memoria ID): {fuente3.decode()}")

    # 4. Combinar y Hashear todas las fuentes juntas
    hash_object = hashlib.sha256()
    hash_object.update(fuente1)
    hash_object.update(fuente2)
    hash_object.update(fuente3)

    hash_digest = hash_object.digest()

    # 5. Convertir el hash final en un entero
    semilla_int_final = int.from_bytes(hash_digest, 'big')

    # 6. Aplicar esta semilla caótica al módulo 'random'
    random.seed(semilla_int_final)
    print("Semilla caótica aplicada a 'random'.\n")


# FUNCIÓN cifrar() - Generar texto cifrado
def cifrar():
    global PALABRA_GUIA, FRASE_CIFRADA
    cifrada = []
    # Generar salto_aleatorio (desplazamiento de César)
    salto = random.randint(1, 25)
    fraseMinuscula = FRASE.lower()
    # Seleccionar PALABRA_GUIA con selectGuia()
    PALABRA_GUIA = selectGuia(fraseMinuscula)

    # Recorrer cada carácter de la frase original
    for letra in fraseMinuscula:
        char = ord(letra)
        if char != 32:  # Para espacios: copiar tal cual
            # Para letras: aplicar desplazamiento salto_aleatorio
            if char == 241 or char == 209:  # Caso especial para 'ñ'
                char = definirChar(110 + salto)
            else:
                char = definirChar(char + salto)
        cifrada.append(chr(char))  # Añadir carácter a lista cifrada

    FRASE_CIFRADA = "".join(cifrada)  # Unir lista en FRASE_CIFRADA

# Seleccionar palabra guía (mínimo 3 letras)
def selectGuia(frase):
    palabra = ""
    while len(palabra) < 3:
        lista_palabras = frase.split()
        palabra = random.choice(lista_palabras)
    return palabra

# Función auxiliar para manejo de caracteres
def definirChar(ascii):
    if ascii >= 123:    # Wrap-around si pasa de 'z'
        return ascii - 122 + 96
    if ascii < 97:      # Wrap-around si es menor que 'a'
        return 122 - (96 - ascii)
    return ascii

# FUNCIÓN descifradoCesar() - Recuperar salto y descifrar
def descifradoCesar():
    # Crear lista wordsWithLen (palabras con misma longitud que PALABRA_GUIA)
    wordsWithLen = []
    for palabra in FRASE_CIFRADA.split():
        if len(palabra) == len(PALABRA_GUIA):
            wordsWithLen.append(palabra)

    # Inicializar desplazamiento en None
    desplazamiento = None

    # Para cada palabra en wordsWithLen:
    for palabra in wordsWithLen:
        if not palabra or not PALABRA_GUIA:
            continue

        # Calcular salto (basado en primera letra)
        salto = ord(palabra[0]) - ord(PALABRA_GUIA[0])
        if salto < 0:
            salto += 26

        # Asumimos que coincide hasta que se demuestre lo contrario
        coincidencia_total = True

        # Iterar cada letra de la palabra guía
        for i in range(len(PALABRA_GUIA)):
            letra_cifrada = palabra[i]
            letra_guia_original = PALABRA_GUIA[i]

            char_descifrado = definirChar(ord(letra_cifrada) - salto)

            if chr(char_descifrado) != letra_guia_original:
                coincidencia_total = False
                break

        if coincidencia_total:
            desplazamiento = salto
            break

    # descifrar_after_loop
    if desplazamiento is None:
        return ""  # No se encontró desplazamiento

    # Si desplazamiento es diferente a None: descifrar texto completo
    diccionario = {}
    for i in range(97, 123):  # Crear diccionario de descifrado
        diccionario[chr(i)] = chr(definirChar(i - desplazamiento))

    # Aplicar descifrado a toda la frase
    texto_descifrado = ""
    for letra in FRASE_CIFRADA:
        if letra == " ":  # Respetar espacios
            texto_descifrado += " "
        elif letra in diccionario:
            texto_descifrado += diccionario[letra]
        else:
            texto_descifrado += letra

    # Mostrar resultados
    print("\nTexto cifrado:", FRASE_CIFRADA)
    print("Palabra guia:", PALABRA_GUIA)
    print("Desplazamiento encontrado:", desplazamiento)
    print("Texto descifrado:", texto_descifrado, "\n")


# FLUJO PRINCIPAL

# INICIO
generar_semilla_caotica()

cifrar()           # Producir FRASE_CIFRADA y PALABRA_GUIA
descifradoCesar()  # Recuperar salto y descifrar
# FIN

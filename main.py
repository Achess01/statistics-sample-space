import numpy as np
import pandas as pd
import itertools
from itertools import permutations, product
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('pdf')


def main():
    numeros = [40, 45, 50]
    probabilidades = [0.20, 0.30, 0.50]
    tamaño_grupo = 4
    calcular_combinaciones(numeros, probabilidades, tamaño_grupo)
    # numbers = [10, 11, 12, 13, 14, 15]
    # # TODO: Create csv file
    # get_means_histogram(numbers, 3, repetition=True)


def get_means_histogram(numbers: list, size: int, repetition: bool = False):
    means = distribution_of_means(numbers, size, repetition)
    plt.hist(means, bins=len(set(means)), color='blue', edgecolor='black')
    plt.savefig(f'means_histogram_{size}.png')


def sample_space_no_repetition(numbers: list, size: int):
    perms = permutations(numbers, size)
    return list(perms)


def sample_space_wit_repetition(numbers: list, size: int):
    perms = product(numbers, repeat=size)
    return list(perms)


def distribution_of_means(numbers: list, size: int, repetition: bool = False):
    perms = sample_space_no_repetition(
        numbers, size) if not repetition else sample_space_wit_repetition(numbers, size)
    means = [round(sum(perm)/size, 2) for perm in perms]

    return means


def calcular_combinaciones(numeros, probabilidades, tamaño_grupo, nombre_archivo="combinaciones.xlsx"):

    combinaciones = list(itertools.product(numeros, repeat=tamaño_grupo))

    probabilidades_conjuntas = [np.prod([probabilidades[numeros.index(
        x)] for x in combinacion]) for combinacion in combinaciones]

    medias = [np.mean(combinacion) for combinacion in combinaciones]
    varianzas = [np.var(combinacion, ddof=1) for combinacion in combinaciones]

    p_header = ",".join([f"x{i+1}" for i in range(tamaño_grupo)])

    headers = [
        f"x{i+1}" for i in range(tamaño_grupo)] + [f"p({p_header})", "media", "varianza"]
    data = [list(combinaciones[i]) + [probabilidades_conjuntas[i],
                                      medias[i], varianzas[i]] for i in range(len(combinaciones))]
    df = pd.DataFrame(data, columns=headers)

    df.to_excel(nombre_archivo, index=False, float_format="%.5f")

    print(f"Archivo '{nombre_archivo}' generado con éxito.")


if __name__ == '__main__':
    main()

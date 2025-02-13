from itertools import permutations, product
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('pdf')

def main():
    numbers = [10, 11, 12, 13, 14, 15]
    # TODO: Create csv file
    get_means_histogram(numbers, 3, repetition=True)


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
    perms = sample_space_no_repetition(numbers, size) if not repetition else sample_space_wit_repetition(numbers, size)
    means = [round(sum(perm)/size, 2) for perm in perms]

    return means

if __name__ == '__main__':
    main()

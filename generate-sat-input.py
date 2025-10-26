import random
from itertools import combinations, product
from random import shuffle


def output_generated_sat_input(set_size: int, num_subsets: int):
    full_set_tuple: tuple[int] = tuple(range(1, set_size + 1))
    first_set_size: int = random.randint(1, set_size)

    first_set: set[int] = set(random.sample(full_set_tuple, first_set_size))
    second_set: set[int] = set(full_set_tuple) - first_set

    generate_subsets(first_set, second_set, num_subsets)

def output_generate_probable_unsat_input(set_size: int, num_of_subsets: int):
    full_set_tuple: tuple[int] = tuple(range(1, set_size + 1))
    first_set_size: int = random.randint(1, set_size)

    first_set: set[int] = set(random.sample(full_set_tuple, first_set_size))
    second_set: set[int] = set(full_set_tuple) - first_set

    generate_subsets(first_set, second_set, num_of_subsets)
    print(" ".join(map(str, first_set)))
    print(" ".join(map(str, second_set)))


def generate_subsets(first_set: set[int], second_set: set[int], num_subsets: int):
    generated: int = 0

    first_set_counts: list[int] = list(range(1, len(first_set) + 1))
    second_set_counts: list[int] = list(range(1, len(second_set) + 1))

    shuffle(first_set_counts)
    shuffle(second_set_counts)
    for first_set_chosen_count, second_set_chosen_count in product(first_set_counts, second_set_counts):
        for from_first_set in combinations(first_set, first_set_chosen_count):
            for from_second_set in combinations(second_set, second_set_chosen_count):
                print(" ".join(map(str, from_first_set + from_second_set)))
                generated += 1
                if generated == num_subsets:
                    return

if __name__ == '__main__':
    # output_generated_sat_input(1000, 10000)
    output_generate_probable_unsat_input(20, 80000)
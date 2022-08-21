import numpy

token_1 = "hello"
token_2 = "kelm"


def levenshtein_distance(token_1: str, token_2: str) -> int:
    distances = numpy.zeros((len(token_1) + 1, len(token_2) + 1))

    for i in range(len(token_1) + 1):
        distances[i, 0] = i

    for j in range(len(token_2) + 1):
        distances[0, j] = j

    print_distances(distances, len(token_1), len(token_2))
    return 0


def print_distances(distances_matrix: numpy.ndarray, row_length: int, column_length: int) -> None:
    for i in range(row_length + 1):
        for j in range(column_length + 1):
            print(int(distances_matrix[i, j]), end=" ")
        print()


levenshtein_distance(token_1, token_2)
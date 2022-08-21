import numpy


# Source: https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
def levenshtein_distance(token_1: str, token_2: str) -> int:
    distances = numpy.zeros((len(token_1) + 1, len(token_2) + 1))

    for i in range(len(token_1) + 1):
        distances[i, 0] = i

    for j in range(len(token_2) + 1):
        distances[0, j] = j

    for i in range(1, len(token_1) + 1):
        for j in range(1, len(token_2) + 1):
            if token_1[i - 1] == token_2[j - 1]:
                distances[i, j] = distances[i - 1, j -1]
            else:
                north_east = distances[i - 1, j - 1]
                east = distances[i, j - 1]
                north = distances[i - 1, j]
                distances[i, j] = min(north_east, east, north) + 1

    print_distances(distances, len(token_1), len(token_2))
    return distances[len(token_1), len(token_2)]


def print_distances(distances_matrix: numpy.ndarray, row_length: int, column_length: int) -> None:
    for i in range(row_length + 1):
        for j in range(column_length + 1):
            print(int(distances_matrix[i, j]), end=" ")
        print()


if __name__ == "__main__":
    token_1 = "kelm"
    token_2 = "hello"
    levenshtein_distance(token_1, token_2)
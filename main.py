def print_out(matrix):
    for el in matrix:
        print(el)


def minus(matrix, line1, line2, multiplier):
    for i in range(len(matrix[line1 - 1])):
        matrix[line1 - 1][i] -= matrix[line2 - 1][i] * multiplier
    return matrix


if __name__ == "__main__":
    size = int(input("размер матрицы: "))
    matrix = []
    for _ in range(size):
        matrix.append(list(map(int, input("> ").split(" "))))
    print_out(matrix)
    while True:
        action = input("действие [ строка1 - строка2 * коэф ] > ")  # N - M * multiplier
        if action == "done":
            break
        matrix = minus(
            matrix,
            int(action.split(" - ")[0]),
            int(action.split(" - ")[1].split(" * ")[0]),
            int(action.split(" - ")[1].split(" * ")[1]),
        )
        print_out(matrix)

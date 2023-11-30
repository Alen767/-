def calculate_max_queens(n, cache={}):
    if n <= 3:
        return n - 1

    if n in cache:
        return cache[n]

    max_queens = n
    for i in range(1, n-1):
        max_queens = max(max_queens, calculate_max_queens(i) + 1 + calculate_max_queens(n-i-1))

    cache[n] = max_queens
    return max_queens


def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline())

    max_queens = calculate_max_queens(n)

    with open('output.txt', 'w') as file:
        file.write(str(max_queens))

if __name__ == "__main__":
    main()
def buildpyramid(n):
    if not (1 <= n <= 10):
        print("Помилка: введіть ціле число від 1 до 10.")
        return

    for i in range(1, n + 1):
        spaces = " " * (n - i)
        numbers = str(i) * (2 * i - 1)
        print(spaces + numbers)
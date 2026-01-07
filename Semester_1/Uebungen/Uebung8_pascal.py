def pascal_triangle(expansions):

    def c(n, k):
        if k == 0 or k == n:
            return 1
        return c(n - 1, k - 1) + c(n - 1, k)

    rows = expansions + 1
    if rows <= 0:
        return

    max_val = c(rows - 1, (rows - 1) // 2)
    width = len(str(max_val))

    for r in range(rows):
        indent = ' ' * ((rows - r - 1) * (width + 1) // 2)
        print(indent, end='')
        for k in range(r + 1):
            print(str(c(r, k)).rjust(width), end=' ')
        print()


if __name__ == "__main__":
    try:
        n = int(input("Anzahl der Erweiterungen (0 = nur 1): "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Ungültige Eingabe, verwende Standardwert 3")
        n = 3
    pascal_triangle(n)

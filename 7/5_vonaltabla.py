#!/usr/bin/env python3

from keres import *

PONTOK = {
    (0, 0),
    (0, 4),
    (1, 3),
    (1, 6),
    (2, 2),
    (3, 5),
    (4, 1),
    (4, 4),
    (5, 2),
    (5, 7),
    (6, 0),
    (6, 5),
    (7, 3),
    (7, 7),
}

ROWS, COLS = 8, 8


def idx(i, j):
    return i * COLS + j


class VonalTabla(Feladat):
    def __init__(self, kezdo):
        self.kezdo = kezdo

    def celteszt(self, allapot):
        tabla, i, j, d = allapot
        if "L" not in tabla and "0" not in tabla:
            return False
        if tabla.count("0") + tabla.count("P") > 0:
            return False
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if ni == 0 and nj == 0:
                return True
        return False

    def rakovetkezo(self, allapot):
        tabla, ci, cj, d = allapot
        lista = list(tabla)

        for di, dj, nd in [
            (-1, 0, "FEL"),
            (1, 0, "LE"),
            (0, -1, "BAL"),
            (0, 1, "JOBB"),
        ]:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < ROWS and 0 <= nj < COLS):
                continue
            if lista[idx(ni, nj)] == "L":
                continue
            if lista[idx(ci, cj)] == "P" and nd == d:
                continue

            uj = lista[:]
            uj[idx(ci, cj)] = "L"
            yield (f"({ci},{cj})->({ni},{nj})", (tuple(uj), ni, nj, nd))


def heurisztika(csucs):
    tabla, i, j, d = csucs.allapot
    return tabla.count("0") + tabla.count("P")


def main():
    tabla = []
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) in PONTOK:
                tabla.append("P")
            else:
                tabla.append("0")
    tabla[idx(0, 0)] = "L"
    kezdo = (tuple(tabla), 0, 0, "JOBB")

    feladat = VonalTabla(kezdo)

    print("A csillag")
    result = a_csillag(feladat, heurisztika)
    if result:
        print(result.megoldas())
        print("Lépések száma:", len(result.megoldas()))
    else:
        print("Nincs megoldas")


if __name__ == "__main__":
    main()

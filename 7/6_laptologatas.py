#!/usr/bin/env python3

from keres import *


class Laptologatas(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self, allapot):
        lista = list(allapot)
        cols = 7
        for ures, ertek in enumerate(lista):
            if ertek == 0:
                i, j = ures // cols, ures % cols
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 4 and 0 <= nj < 7:
                        akt = ni * cols + nj
                        if lista[akt] not in ("X", 0):
                            uj = lista[:]
                            uj[ures], uj[akt] = uj[akt], uj[ures]
                            # print(uj[0:7])
                            # print(uj[7:14])
                            # print(uj[14:21])
                            # print(uj[21:28])
                            # print("\033[2A", end="")
                            yield (f"{akt}->{ures}", tuple(uj))


def heurisztika(csucs):
    allapot = csucs.allapot
    return sum(
        1
        for i in range(len(allapot))
        if allapot[i] not in ("X", 0) and allapot[i] != cel[i]
    )


def main():
    global cel
    # fmt: off
    kezdo = (
        'X', 'X', 'X',  4, 'X', 'X', 'X',
        'X', 'X',  9,  11,  7, 'X', 'X',
        'X', 10,   8,  14,  6,  5, 'X',
         2,   0,   0,  13,  1,  3,  12,
    )

    cel = (
        'X', 'X', 'X',  1, 'X', 'X', 'X',
        'X', 'X',  2,   3,  4, 'X', 'X',
        'X',  5,   6,   7,  8,  9, 'X',
        10,  11,  12,  13, 14,  0,   0,
    )
    # fmt: on

    feladat = Laptologatas(kezdo, cel)
    """
    print("Szelessegi grafkereso")
    result1 = szelessegi_grafkereso(feladat)
    print(result1.megoldas())
    print("Lépések száma:", len(result1.megoldas()))

    print("Melysegi grafkereso")
    result2 = melysegi_grafkereso(feladat)
    print(result2.megoldas())
    print("Lépések száma:", len(result2.megoldas()))
    """
    print("A csillag")
    result3 = a_csillag(feladat, heurisztika)
    print(result3.megoldas())
    print("Lépések száma:", len(result3.megoldas()))


if __name__ == "__main__":
    main()

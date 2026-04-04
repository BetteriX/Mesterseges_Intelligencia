#!/usr/bin/env python3

from keres import *


class Laptologatas(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot == self.cél

    def rákövetkező(self, állapot):
        lista = list(állapot)
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


def heurisztika(csúcs):
    állapot = csúcs.állapot
    return sum(
        1
        for i in range(len(állapot))
        if állapot[i] not in ("X", 0) and állapot[i] != cel[i]
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
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    print("Lépések száma:", len(result1.megoldás()))

    print("Melysegi grafkereso")
    result2 = mélységi_gráfkereső(feladat)
    print(result2.megoldás())
    print("Lépések száma:", len(result2.megoldás()))
    """
    print("A csillag")
    result3 = a_csillag(feladat, heurisztika)
    print(result3.megoldás())
    print("Lépések száma:", len(result3.megoldás()))


if __name__ == "__main__":
    main()

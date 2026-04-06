#!/usr/bin/env python3

from keres import *


class Sakk(Feladat):
    def __init__(self, kezdő, cél):
        self.kezdő = kezdő
        self.cél = cél

    def célteszt(self, állapot):
        return állapot[0] == self.cél

    def rákövetkező(self, állapot):
        utodok = []
        tábla = állapot[0]
        i, j = állapot[1]

        lepesek = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]

        for di, dj in lepesek:
            uj_i = i + di
            uj_j = j + dj

            if (0 <= uj_i <= 7) and (0 <= uj_j <= 7) and (tábla[uj_i][uj_j] == 0):
                uj_tabla_lista = [list(sor) for sor in tábla]
                uj_tabla_lista[uj_i][uj_j] = 1

                uj_tabla = tuple(tuple(sor) for sor in uj_tabla_lista)

                uj_pozicio = (uj_i, uj_j)
                uj_allapot = (uj_tabla, uj_pozicio)

                utodok.append((f"lépés({uj_i},{uj_j})", uj_allapot))

        return utodok

    def heurisztika(self, csúcs):
        tábla = csúcs.állapot[0]
        nullak_szama = 0
        for sor in tábla:
            nullak_szama += sor.count(0)
        return nullak_szama


def main():
    kezdo_tabla = (
        ("x", 1, 0, 0, 0, 0, 0, "x"),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0),
        ("x", 0, 0, 0, 0, 0, 0, "x"),
    )

    cel_tabla = (
        ("x", 1, 1, 1, 1, 1, 1, "x"),
        (1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1),
        (1, 1, 1, 1, 1, 1, 1, 1),
        ("x", 1, 1, 1, 1, 1, 1, "x"),
    )

    kezdo_pozicio = (0, 1)
    kezdo_allapot = (kezdo_tabla, kezdo_pozicio)

    feladat = Sakk(kezdo_allapot, cel_tabla)

    result1 = best_first(feladat, feladat.heurisztika)
    print("A Best-First kereső: ")
    print(result1.megoldás())

    """
    ut = result1.út()
    ut.reverse()
    print(ut)
    """


if __name__ == "__main__":
    main()

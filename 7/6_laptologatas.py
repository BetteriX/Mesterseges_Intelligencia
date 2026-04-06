#!/usr/bin/env python3

from keres import *


class Laptologatas(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c
        self.iranyok = [
            (0, 2, "Jobb"),
            (0, -2, "Bal"),
            (1, 1, "Jobb-Le"),
            (-1, 1, "Jobb-Fel"),
            (1, -1, "Bal-Le"),
            (-1, -1, "Bal-Fel"),
        ]

    def rákövetkező(self, állapot):
        ures_helyek = []
        for s in range(len(állapot)):
            for o in range(len(állapot[s])):
                if állapot[s][o] == 0:
                    ures_helyek.append((s, o))

        for us, uo in ures_helyek:
            for ls, lo, nev in self.iranyok:
                r_lapka, c_lapka = us - ls, uo - lo

                if 0 <= r_lapka < len(állapot) and 0 <= c_lapka < len(állapot[0]):
                    ertek = állapot[r_lapka][c_lapka]

                    if isinstance(ertek, int) and ertek > 0:
                        lista_m = [list(sor) for sor in állapot]

                        lista_m[us][uo] = ertek
                        lista_m[r_lapka][c_lapka] = 0

                        uj_allapot = tuple(tuple(sor) for sor in lista_m)

                        muvelet = f"Lapka {ertek} mozgatása ide: ({us},{uo}) [{nev}]"
                        yield muvelet, uj_allapot

    def célteszt(self, állapot):
        return állapot == self.cél


def heurisztika(csúcs, feladat):
    h = 0
    akt_allapot = csúcs.állapot
    cel_allapot = feladat.cél

    for n in range(len(akt_allapot)):
        for m in range(len(akt_allapot[n])):
            akt_ertek = akt_allapot[n][m]
            if isinstance(akt_ertek, int) and akt_ertek > 0:
                if akt_ertek != cel_allapot[n][m]:
                    h += 1
    return h


def main():
    kezdo = (
        ("x", "x", "x", 4, "x", "x", "x"),
        ("x", "x", 9, 11, 7, "x", "x"),
        ("x", 10, 8, 14, 6, 5, "x"),
        (2, 0, 0, 13, 1, 3, 12),
    )

    cel = (
        ("x", "x", "x", 1, "x", "x", "x"),
        ("x", "x", 2, 3, 4, "x", "x"),
        ("x", 5, 6, 7, 8, 9, "x"),
        (10, 11, 12, 13, 14, 0, 0),
    )

    feladat = Laptologatas(kezdo, cel)
    """
    print("Szelessegi grafkereso")
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())

    print("Melysegi grafkereso")
    result2 = mélységi_gráfkereső(feladat)
    print(result2.megoldás())
    """

    print("Best-First")
    result3 = best_first(feladat, lambda cs: heurisztika(cs, feladat))
    print(result3.megoldás())
    print("Lépések száma:", len(result3.megoldás()))


if __name__ == "__main__":
    main()

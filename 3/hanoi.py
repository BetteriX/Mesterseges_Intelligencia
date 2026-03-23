#!/usr/bin/env python3

from keres import *


class Hanoi:
    def __init__(self, kezdo: tuple, cel: tuple):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, a: tuple):  # a=(a1, a2, ..., an)
        return a == self.cel

    def rakovetkezo(self, a: tuple):
        gyerekek = []
        n = len(a)  # Korongok száma

        for melyiket in range(0, n):
            for hova in ["P", "Q", "R"]:  # Átrak melyiket hova
                tmp = True
                if a[melyiket] != hova:
                    for i in range(0, melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            tmp = True
                        else:
                            tmp = False
                            break
                else:
                    tmp = False

            if tmp:
                uj_allapot = list(a)
                uj_allapot[melyiket] = hova
                gyerekek.append(tuple(uj_allapot))

        return gyerekek


def heurisztika1(csucs):
    a = csucs.allapot
    cel = ("R", "R", "R")
    n = len(a)
    for i in range(len(a) - 1, -1, -1):
        if a[i] == cel[i]:
            n = n - 1
        else:
            break

    return 2**n - 1


def main():
    feladat = Hanoi(("P", "P", "P", "P", "P"), ("R", "R", "R", "R", "R"))

    result1 = melysegi_fakereso(feladat)
    print(result1.megoldas())
    print(feladat.rakovetkezo(("P", "P")))

    print("best-first")
    result2 = best_first(feladat, heurisztika1)
    print(result2.megoldas())


if __name__ == "__main__":
    main()

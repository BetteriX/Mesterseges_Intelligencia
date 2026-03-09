#!/usr/bin/env python3


import numpy as np


class Kiralynok:
    def __init__(self, ke, c):
        self.kezdo = ke  # (tábla, kezdő sor)
        self.cel = c  # utolsó sor index
        self.n = len(ke[0])  # tábla mérete (8)

    def celteszt(self, a):
        # ha az aktuális sor = cél, minden királynő elhelyezve
        return a[1] == self.cel

    def rakovetkezo(self, t):  # ← itt az osztály részeként
        gyerekek = []
        s = t[1]
        a = t[0].copy()

        for i in range(self.n):
            elofeltetel = True

            # oszlop ellenőrzés
            for row in range(s - 1):  # s-1, mert kezdő sor 1
                if a[row, i] == 1:
                    elofeltetel = False
                    break

            # diagonális ellenőrzés abs segítségével
            if elofeltetel:
                for row in range(s - 1):
                    for col in range(self.n):
                        if a[row, col] == 1 and abs((s - 1) - row) == abs(i - col):
                            elofeltetel = False
                            break
                    if not elofeltetel:
                        break

            if elofeltetel:
                uj_allpot = a.copy()
                uj_allpot[s - 1, i] = 1
                gyerekek.append((uj_allpot, s + 1))

        return gyerekek


def main():
    tabla = np.zeros((8, 8), dtype=int)
    feladat = Kiralynok((tabla, 1), 9)  # kezdő sor 1, cél sor 9

    allapotok = [feladat.kezdo]

    while allapotok:
        uj = []
        for a in allapotok:
            if feladat.celteszt(a):
                print(a[0])
                return
            uj += feladat.rakovetkezo(a)
        allapotok = uj


if __name__ == "__main__":
    main()

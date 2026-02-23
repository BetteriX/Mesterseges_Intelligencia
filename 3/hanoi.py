#!/usr/bin/env python3


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


def main():
    feladat = Hanoi(("P", "P", "P", "P", "P"), ("R", "R", "R", "R", "R"))


if __name__ == "__main__":
    main()

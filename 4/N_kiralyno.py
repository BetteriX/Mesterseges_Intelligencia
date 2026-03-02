#!/usr/bin/env python3


class Kiralyno:
    def __init__(self, kezdo: tuple, cel: int):
        self.kezdo = kezdo
        self.cel = cel
        self.N = len(kezdo) - 1

    def celteszt(self, a) -> bool:  # a = (a1, a2,..., an, s)
        return a[self.N] == self.cel

    def rakovetkezo(self, a: tuple) -> list:
        gyerekek = []
        s = a[self.N]
        for i in range(1, self.N + 1):
            elofeltetel = True  # lerak (s,i) alkalmazható?
            for m in range(1, s):  # bármely m < s sorok esetén:
                if a[m - 1] != i and abs(m - s) != abs(a[m - 1] - i):
                    elofeltetel = True
                else:
                    elofeltetel = False
                    break

            if elofeltetel:
                uj_allapot = list(a)
                uj_allapot[s - 1] = i
                uj_allapot[self.N] = s + 1

                gyerekek.append(tuple(uj_allapot))

        return gyerekek


def main():
    feladat = Kiralyno((0, 0, 0, 0, 0, 0, 0, 0, 1), 9)

    print(feladat.rakovetkezo(feladat.kezdo))


if __name__ == "__main__":
    main()

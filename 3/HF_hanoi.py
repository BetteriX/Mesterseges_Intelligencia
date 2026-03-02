#!/usr/bin/env python3


class Hanoi:
    def init(self, ke: tuple, c: tuple):
        self.ke = ke
        self.c = c

    def celtest(self, a: tuple) -> bool:
        return a == self.c

    def rakovetkezo(self, a: tuple) -> list:  # i = melyikrol, j = hova
        gyerekek = []
        for i in range(3):
            for j in range(3):
                if i == j or not a[i]:
                    continue

                uj = [list(r) for r in a]
                korong = uj[i][0]  # min

                if not uj[j] or korong < uj[j][0]:
                    uj[i].pop(0)
                    uj[j].insert(0, korong)
                    gyerekek.append(tuple(uj))
        return gyerekek


def main():
    pass


if __name__ == "__main__":
    main()

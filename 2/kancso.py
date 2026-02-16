#!/usr/bin/env python3


class Kancsok:
    def __init__(self, kezdo: tuple, cel: int):
        self.kezdo = kezdo
        self.cel = cel
        self.max1 = 3
        self.max2 = 5
        self.max3 = 8

    def celteszt(self, a: tuple):  # a = (a1,a2,a3) állapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a: tuple):
        gyerekek = []
        a1, a2, a3 = a

        # tölt 1,2
        if a1 != 0 and a2 != self.max2:
            T = min(a1, self.max2 - a2)
            gyerekek.append(("tölt 1-ből 2-be", (a1 - T, a2 + T, a3)))

        # tölt 1,3
        if a1 != 0 and a3 != self.max3:
            T = min(a1, self.max3 - a3)
            gyerekek.append(("tölt 1-ből 3-be", (a1 - T, a2, a3 + T)))

        # tölt 2,1
        if a2 != 0 and a1 != self.max1:
            T = min(a2, self.max1 - a1)
            gyerekek.append(("tölt 2-ből 1-be", (a1 + T, a2 - T, a3)))

        # tölt 2,3
        if a2 != 0 and a3 != self.max3:
            T = min(a2, self.max3 - a3)
            gyerekek.append(("tölt 2-ből 3-be", (a1 + T, a2, a3 - T)))

        # tölt 3,1
        if a3 != 0 and a1 != self.max1:
            T = min(a3, self.max1 - a1)
            gyerekek.append(("tölt 1-ből 2-be", (a1 - T, a2 + T, a3)))

        return gyerekek


def main():
    feladat = Kancsok((0, 0, 8), 4)


if __name__ == "__main__":
    main()

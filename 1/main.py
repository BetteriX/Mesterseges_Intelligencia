#!/usr/bin/env python3

import math


def szokoevek(ev1: int, ev2: int) -> list:
    eredmeny = []
    for ev in range(ev1, ev2 + 1):
        if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
            eredmeny.append(ev)

    return eredmeny


def is_palindrom(szam: int) -> bool:
    eredeti = szam
    forditott = 0

    while szam > 0:
        szj = szam % 10
        szam = szam // 10
        forditott = forditott * 10 + szj

    return eredeti == forditott


# páros számok négyzete
def paros_negyzetek(szamok: list) -> list:
    return [x * x for x in szamok if x % 2 == 0]


def min_max(szamok: list) -> tuple:
    return (min(szamok), max(szamok))


class Hallgato:
    def __init__(self, nev: str, nkod: str):
        self.nev = nev
        self.nkod = nkod
        self.jegyek = []

    def jegy_hozzad(self, jegy: int):
        if 1 <= jegy <= 5:
            self.jegyek.append(jegy)

    def atlag(self) -> float:
        if not self.jegyek:
            return 0.0

        # return sum(self.jegyek) / len(self.jegyek)
        return math.avg(self.jegyek)

    def __str__(self):
        return f"{self.nev} ({self.nkod}) - atlag: {self.atlag()}"


def main():
    print(szokoevek(1890, 2024))

    print(is_palindrom(12321))

    print(paros_negyzetek([2, 3, 5, 7, 10]))

    min_max_result = min_max([1, 3, 4, 9, -10])
    print(min_max_result)

    tuple_pelda = (12, "alma", [1, 3, 4], "korte")
    print(tuple_pelda)

    tmp_list = list(tuple_pelda)
    tmp_list[0] = "szilva"
    tuple_modosult = tuple(tmp_list)
    print(tuple_modosult)

    h = Hallgato("Den Ella", "ABCD2")
    h.jegy_hozzad(5)
    h.jegy_hozzad(3)
    h.jegy_hozzad(1)

    print(h)


if __name__ == "__main__":
    main()

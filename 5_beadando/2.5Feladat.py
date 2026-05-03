#!/usr/bin/env python3

from my_jatek import *


class KiralynoJatek(Jatek):
    """
    Királynő játék:
    Csak 1 mezőt lehet lépni balra, le, vagy átlósan balra-le.
    """

    def __init__(self, n=8, start_pos=None):
        update(self, n=n)
        if start_pos is None:
            start_pos = (n, n)

        self.kezdo = Struct(pos=start_pos, kovetkezik="A", eredmeny=0)

    def legalis_lepesek(self, allapot):
        """Szomszédos 3 irányba léphet."""
        x, y = allapot.pos
        lepesek = []

        # 1. Egyet balra (ha nem az első oszlopban van)
        if y > 1:
            lepesek.append((x, y - 1))

        # 2. Egyet lefelé (ha nem az első sorban van)
        if x > 1:
            lepesek.append((x - 1, y))

        # 3. Egyet átlósan balra le
        if x > 1 and y > 1:
            lepesek.append((x - 1, y - 1))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        eredmeny = 0

        # Az nyer, aki rálép az (1, 1) célmezőre
        if lepes == (1, 1):
            eredmeny = 1 if allapot.kovetkezik == "A" else -1

        return Struct(
            pos=lepes,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=eredmeny,
        )

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.pos == (1, 1)

    def kiir(self, allapot):
        x_q, y_q = allapot.pos
        for r in range(self.n, 0, -1):
            for c in range(1, self.n + 1):
                if r == x_q and c == y_q:
                    print("Q", end=" ")
                elif r == 1 and c == 1:
                    print("X", end=" ")  # Célmező
                else:
                    print(".", end=" ")
            print()
        print(
            f"Pozíció: {allapot.pos} | Következik: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}\n "
        )


def main():
    jatek = KiralynoJatek(n=6)
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()

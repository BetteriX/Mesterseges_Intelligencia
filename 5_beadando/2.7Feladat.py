#!/usr/bin/env python3

from my_jatek import *


class JatekTabla(Jatek):
    def __init__(self, n=5):
        update(self, n=n)
        self.kezdo = Struct(tabla={}, kovetkezik="A", eredmeny=0)

    def legalis_lepesek(self, allapot):
        if allapot.eredmeny != 0:
            return []
        return [
            (sor, oszlop)
            for sor in range(1, self.n + 1)
            for oszlop in range(1, self.n + 1)
            if (sor, oszlop) not in allapot.tabla
        ]

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        uj_tabla = allapot.tabla.copy()
        uj_tabla[lepes] = allapot.kovetkezik

        sor, oszlop = lepes
        szomszedok = [
            (sor - 1, oszlop),
            (sor + 1, oszlop),
            (sor, oszlop - 1),
            (sor, oszlop + 1),
        ]

        azonos_szomszedok = 0
        for sz in szomszedok:
            if uj_tabla.get(sz) == allapot.kovetkezik:
                azonos_szomszedok += 1

        uj_eredmeny = 0
        if azonos_szomszedok == 4:
            uj_eredmeny = -1 if allapot.kovetkezik == "A" else 1
        elif len(uj_tabla) == self.n * self.n:
            uj_eredmeny = 0

        return Struct(
            tabla=uj_tabla,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=uj_eredmeny,
        )

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        # A játék akkor ér véget, ha van eredmény VAGY betelt a tábla
        return allapot.eredmeny != 0 or len(allapot.tabla) == self.n * self.n

    def kiir(self, allapot):
        for sor in range(1, self.n + 1):
            for oszlop in range(1, self.n + 1):
                val = allapot.tabla.get((sor, oszlop), ".")
                print(val, end=" ")
            print()
        print(f"Következik: {allapot.kovetkezik} | Eredmény: {allapot.eredmeny}\n")


def main():
    jatek = JatekTabla()
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()

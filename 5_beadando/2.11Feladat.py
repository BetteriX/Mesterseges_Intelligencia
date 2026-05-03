#!/usr/bin/env python3

from my_jatek import *


class KavicsKupac(Jatek):
    def __init__(self, kupacok):
        update(self, kezdo_kupacok=kupacok)
        self.kezdo = Struct(kupacok=kupacok, kovetkezik="A", eredmeny=0)

    def legalis_lepesek(self, allapot):
        """Kiszámítja az összes olyan elvételt, amivel osztható a kupac."""
        lepesek = []
        for i, n in enumerate(allapot.kupacok):
            if n > 1:
                for mennyi in range(1, n):
                    if n % mennyi == 0:
                        lepesek.append((i, mennyi))
        return lepesek

    def lep(self, lepes, allapot):
        """Végrehajtja az elvételt."""
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        i, mennyi = lepes
        uj_kupacok = list(allapot.kupacok)
        uj_kupacok[i] -= mennyi
        uj_kupacok = tuple(uj_kupacok)

        uj_allapot = Struct(
            kupacok=uj_kupacok,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=0,
        )

        # Ha a következő játékos nem tud lépni, az aktuális nyert
        if not self.legalis_lepesek(uj_allapot):
            uj_allapot.eredmeny = 1 if allapot.kovetkezik == "A" else -1

        return uj_allapot

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """A játék véget ér, ha nincs több legális lépés."""
        return not self.legalis_lepesek(allapot)

    def kiir(self, allapot):
        print(
            f"Kupacok: {allapot.kupacok} | Soron jön: {allapot.kovetkezik} Eredmény:{allapot.eredmeny}"
        )


def main():
    jatek = KavicsKupac(kupacok=(5, 6, 3, 5))

    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()

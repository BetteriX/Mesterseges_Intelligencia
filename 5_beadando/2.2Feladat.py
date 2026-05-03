#!/usr/bin/env python3

from my_jatek import *


class KavicsKupac(Jatek):
    def __init__(self, n, m):
        update(self, n=n, m=m)
        self.kezdo = Struct(
            kupacok=(n, m),
            kovetkezik="A",
            eredmeny=0,
        )

    def legalis_lepesek(self, allapot):
        n, m = allapot.kupacok
        lepesek = []

        # 1. Elvétel az első kupacból
        for mennyi in range(1, n + 1):
            lepesek.append(("K1", mennyi))

        # 2. Elvétel a második kupacból
        for mennyi in range(1, m + 1):
            lepesek.append(("K2", mennyi))

        # 3. Elvétel mindkettőből ugyanannyit
        for mennyi in range(1, min(n, m) + 1):
            lepesek.append(("K12", mennyi))

        return lepesek

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        melyik, mennyi = lepes
        n, m = allapot.kupacok

        if melyik == "K1":
            uj_kupacok = (n - mennyi, m)
        elif melyik == "K2":
            uj_kupacok = (n, m - mennyi)
        else:  # K12
            uj_kupacok = (n - mennyi, m - mennyi)

        # Az nyer, aki az utolsót veszi el (aki 0,0-ra lép)
        eredmeny = 0
        if uj_kupacok == (0, 0):
            eredmeny = 1 if allapot.kovetkezik == "A" else -1

        return Struct(
            kupacok=uj_kupacok,
            kovetkezik=if_(allapot.kovetkezik == "A", "B", "A"),
            eredmeny=eredmeny,
        )

    def hasznossag(self, allapot, jatekos):
        """A győzelem értéke 1 a kezdő játékosnak, -1 az ellenfélnek."""
        return if_(jatekos == "A", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        """Véget ér, ha elfogytak a kavicsok."""
        return allapot.kupacok == (0, 0)

    def kiir(self, allapot):
        print(f"Kupac: {allapot.kupacok} | Jön: {allapot.kovetkezik}")


def main():
    jatek = KavicsKupac(5, 7)
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()

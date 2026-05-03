#!/usr/bin/env python3

from my_jatek import *


class HuszarJatek(Jatek):
    def __init__(self, n=8, start_v=(1, 1), start_s=(8, 8)):
        update(self, n=n)
        self.kezdo = Struct(
            vilagos=start_v,
            sotet=start_s,
            tiltott={start_v, start_s},
            kovetkezik="V",
            eredmeny=0,
        )

    def legalis_lepesek(self, allapot):
        """Kiszámítja a soron lévő huszár lehetséges lépéseit."""
        n = self.n
        pos = allapot.vilagos if allapot.kovetkezik == "V" else allapot.sotet
        x, y = pos
        lehetosegek = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1),
        ]

        # Táblán belüli és még nem látogatott mezők
        return [
            p
            for p in lehetosegek
            if 1 <= p[0] <= n and 1 <= p[1] <= n and p not in allapot.tiltott
        ]

    def lep(self, lepes, allapot):
        if type(lepes) is str:
            lepes = make_tuple(lepes)
        uj_tiltott = allapot.tiltott.copy()
        uj_tiltott.add(lepes)

        v_pos = lepes if allapot.kovetkezik == "V" else allapot.vilagos
        s_pos = lepes if allapot.kovetkezik == "S" else allapot.sotet

        uj_allapot = Struct(
            vilagos=v_pos,
            sotet=s_pos,
            tiltott=uj_tiltott,
            kovetkezik=if_(allapot.kovetkezik == "V", "S", "V"),
            eredmeny=0,
        )

        # Ha a következő játékosnak nincs lépése, az aktuális nyert
        if not self.legalis_lepesek(uj_allapot):
            uj_allapot.eredmeny = 1 if allapot.kovetkezik == "V" else -1

        return uj_allapot

    def hasznossag(self, allapot, jatekos):
        return if_(jatekos == "V", allapot.eredmeny, -allapot.eredmeny)

    def levele(self, allapot):
        return allapot.eredmeny != 0

    def kiir(self, allapot):
        print(
            f"V:{allapot.vilagos} S:{allapot.sotet} | Tiltott: {len(allapot.tiltott)} | Jön: {allapot.kovetkezik} | Eredmény:{allapot.eredmeny}"
        )


def main():
    jatek = HuszarJatek(n=8)
    jatssz(jatek, random_jatekos, random_jatekos)


if __name__ == "__main__":
    main()

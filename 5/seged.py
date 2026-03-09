import bisect
import random
import functools


class Varolista:
    def __init__(self):
        pass

    def extend(self, elemek):
        for elem in elemek:
            self.append(elem)


def Verem():
    return []


class Sor(Varolista):
    def __init__(self):
        self.A = []
        self.kezd = 0

    def append(self, elem):
        self.A.append(elem)

    def __len__(self):
        return len(self.A) - self.kezd

    def extend(self, elemek):
        self.A.extend(elemek)

    def pop(self):
        e = self.A[self.kezd]
        self.kezd += 1
        if self.kezd > 5 and self.kezd > len(self.A) / 2:
            self.A = self.A[self.kezd :]
            self.kezd = 0
        return e


class RLElem:
    def __init__(self, ertek, elem):
        self.ertekem = ertek
        self.elemem = elem

    def __lt__(self, másik):
        return self.ertekem < másik.ertekem

    def ertek(self):
        return self.ertekem

    def elem(self):
        return self.elemem


class RendezettLista(Varolista):
    def __init__(self, f):
        self.A = []
        self.f = f

    def append(self, elem):
        pár = RLElem(self.f(elem), elem)
        bisect.insort(self.A, pár)

    def __len__(self):
        return len(self.A)

    def pop(self):
        return self.A.pop(0).elem()


def argmin(lista, fv):
    legjobb = lista[0]
    legjobb_ertek = fv(legjobb)
    for x in lista[1:]:
        x_ertek = fv(x)
        if x_ertek < legjobb_ertek:
            legjobb, legjobb_ertek = x, x_ertek
    return legjobb

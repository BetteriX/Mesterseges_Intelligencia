#!/usr/bin/env python3

import numpy as np


# kereső algoritmusok
def minimax(allapot, jatek):
    jatekos = jatek.kovetkezik(allapot)

    def max_ertek(allapot):
        if jatek.levele(allapot):
            return jatek.hasznossag(allapot, jatekos)
        return max([min_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])

    def min_ertek(allapot):
        if jatek.levele(allapot):
            return jatek.hasznossag(allapot, jatekos)
        return min([max_ertek(s) for (_, s) in jatek.rakovetkezo(allapot)])

    fiai_ertekei = [(a, min_ertek(s)) for (a, s) in jatek.rakovekezo(allapot)]
    lepes, ertek = max(fiai_ertekei, lambda a_s: a_s[1])

    return lepes


def alfabeta_kereses(allapot, jatek, d=4, levagas_teszt=None, kiertekel=None):
    jatekos = jatek.kovetkezik(allapot)

    def max_ertek(allapot, alfa, beta, melyseg):
        if levagas_teszt(allapot, melyseg):
            return kiertekel(allapot)
        v = float("-inf")
        for _, s in jatek.rakovetkezo(allapot):
            v = max(v, min_ertek(s, alfa, beta, melyseg + 1))
            if v >= beta:
                return v
            alfa = max(alfa, v)
        return v

    def min_ertek(allapot, alfa, beta, melyseg):
        if levagas_teszt(allapot, melyseg):
            return kiertekel(allapot)
        v = float("inf")
        for _, s in jatek.rakovetkezo(allapot):
            v = min(v, max_ertek(s, alfa, beta, melyseg + 1))
            if v <= alfa:
                return v
            beta = min(beta, v)
        return v

    levagas_teszt = levagas_teszt or (
        lambda allapot, melyseg: melyseg > d or jatek.levele(allapot)
    )
    kiertekel = kiertekel or (lambda allapot: jatek.hasznossag(allapot, jatekos))
    alfa = float("-inf")
    legjobb_lepes = None
    for a, s in jatek.rakovetkezo(allapot):
        v = min_ertek(s, alfa, float("inf"), 0)
        if v > alfa:
            alfa = v
            legjobb_lepes = a

    return legjobb_lepes


class qlearning:
    def __init__(self, n_states, n_actions, learning_rate):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate

        self.q_table = np.zeros((n_states, n_actions))

    def act(self, state, epsilion):
        random_int = random.uniform(0, 1)

        if random_int > epsilion:
            action = np.argmax(self.q_table[state])
        else:
            action = random.randint(0, self.n_actions - 1)

        return action

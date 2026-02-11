#!/usr/bin/env python3

import math


class Circle:
    def __init__(self, radius: float, rounding: int = 2):
        self.radius = radius
        self.rounding = rounding

    def kerulet(self) -> float:
        return round(2 * self.radius * math.pi, self.rounding)

    def terulet(self) -> float:
        return round(self.radius**2 * math.pi, self.rounding)
        # return math.pow(self.radius,2) * math.pi

    def __str__(self):
        return f"A kör kerülete: {self.kerulet()}, területe: {self.terulet()}"


def main():
    c = Circle(2, 5)

    print(c)


if __name__ == "__main__":
    main()

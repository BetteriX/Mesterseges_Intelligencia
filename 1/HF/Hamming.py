#!/usr/bin/env python3


class Hamming:
    def __init__(self, str1: str, str2: str):
        self.str1 = str1
        self.str2 = str2

    def distance(self) -> int:
        str1Length = len(self.str1)
        str2Length = len(self.str2)

        distance = 0
        if str1Length != str2Length:
            return -1
        else:
            for i in range(0, str1Length):
                if self.str1[i] != self.str2[i]:
                    distance += 1

        return distance


def main():
    Ham = Hamming("toned", "roses")

    print(Ham.distance())

    valami = "gke"
    valami.replace()


if __name__ == "__main__":
    main()

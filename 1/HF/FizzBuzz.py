#!/usr/bin/env python3


class FizzBuzz:
    def __init__(self, totalNum: int):
        self.totalNum = totalNum

    def start(self):
        for i in range(1, self.totalNum + 1):
            fizzbuzz = ""
            if i % 3 == 0:
                fizzbuzz += "fizz"

            if i % 5 == 0:
                fizzbuzz += "buzz"

            if fizzbuzz == "":
                fizzbuzz = i

            print(fizzbuzz)


def main():
    fb = FizzBuzz(10)

    print(fb.start())


if __name__ == "__main__":
    main()

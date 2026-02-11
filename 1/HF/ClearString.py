#!/usr/bin/env python3

import re


def main():
    szoveg = "192.20.246.138:\n\t 6666"

    # clearSzoveg = "".join(szoveg.split())
    clearSzoveg = re.sub(r"\s", "", szoveg)  # \s -> Minden whitespace-t eltüntet
    print(clearSzoveg)


if __name__ == "__main__":
    main()

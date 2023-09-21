import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import stemsep


def main():
    stemsep.main()


if __name__ == "__main__":
    main()
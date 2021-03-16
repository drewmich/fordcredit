#!/usr/bin/env python
import sys
import pytest
import argparse


def main(args):

    try:
        x1 = int(args.x1)
        y1 = int(args.y1)
        x2 = int(args.x2)
        y2 = int(args.y2)

    except ValueError:
        print("Cannot parse arguments as integers", file=sys.stderr)
        return 1

    xDist = abs(x1 - x2)
    yDist = abs(y1 - y2)

    result =  xDist + yDist

    print("Distance between A and B is: " + str(result) )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('x1')
    parser.add_argument('y1')
    parser.add_argument('x2')
    parser.add_argument('y2')
    args = parser.parse_args()
    main(args)

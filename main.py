#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Sample für den ArgParser in Python
#
# Tutorial: https://docs.python.org/3.4/howto/argparse.html
#

import argparse


def init_parser():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")

    return parser


argParser = init_parser()
args = argParser.parse_args()

answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))

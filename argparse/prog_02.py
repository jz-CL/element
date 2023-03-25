# https://docs.python.org/3.10/howto/argparse.html#introducing-positional-arguments

# argumenty pozycyjne - 01

import argparse

# 1
# parser = argparse.ArgumentParser()
# parser.add_argument('echo')
# args = parser.parse_args()
# print(args.echo)

# python prog_02.py
# usage: prog_02.py [-h] echo
# prog_02.py: error: the following arguments are required: echo

# add_argument - metoda do określania wiersza poleceń, które program akceptuje
# wywołanie programu wymaga określenia opcji

# aby pomoc była użyteczna, należy dodć argument pozycyjny
# linię
# parser.add_argument('echo')
# modyfikujemy tak
# parser.add_argument('echo', help='echo the string you use here')

# -------------------------------------------------------------

# 2
# parser = argparse.ArgumentParser()
# parser.add_argument('echo', help='echo the string you use here')
# args = parser.parse_args()
# print(args.echo)

# python prog_02.py -h
# usage: prog_02.py [-h] echo
#
# positional arguments:
#   echo        echo the string you use here
#
# options:
#   -h, --help  show this help message and exit

#  -----------------------------------------------

# 3

# opcje są traktowane jako ciągi znaków

parser = argparse.ArgumentParser()
parser.add_argument('square', help='display a square of a given number', type=int)
args = parser.parse_args()
print(args.square ** 2)

# program reaguje na niewłaściwe dane


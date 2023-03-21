# Combining Positional and Optional arguments

# https://docs.python.org/3.10/howto/argparse.html#combining-positional-and-optional-arguments

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('square', type=int, help='display a square of a given number')
# parser.add_argument('-v', '--verbose', help='increase output verbosity',
#                     action="store_true")
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbose:
#     print(f'the square of {args.verbose} equals {answer}')
# else:
#     print(answer)

# python  prog_05.py
# usage: prog_05.py [-h] [-v] square
# prog_05.py: error: the following arguments are required: square

# python  prog_05.py 4
# 16

# python  prog_05.py 4 --verbose
# the square of True equals 16

# python  prog_05.py --verbose 4
# the square of True equals 16

# -------------------------------------------------

# import argparse
# parser = argparse.ArgumentParser()
#
# parser.add_argument('square', type=int,
#                     help='display a square of a given number')
# parser.add_argument('-v', '--verbosity', help='increase output verbosity',
#                     type=int)
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbosity == 2:
#     print(f'the square of {args.square} equals {answer}')
# elif args.verbosity == 1:
#     print(f'{args.square}^2 == {answer}')
# else:
#     print(answer)

# python  prog_05.py  4
# 16

# python  prog_05.py  4 -v 1
# 4^2 == 16

# python  prog_05.py  4 -v 2
# the square of 4 equals 16


# ta opcja jest będna bo wartość 3 jest niedopuszczalna
# python  prog_05.py  4 -v 3
# 16

# -------------------------------------------------
# choices=[0, 1, 2]

# import argparse
# parser = argparse.ArgumentParser()
#
# parser.add_argument('square', type=int,
#                     help='display a square of a given number')
# parser.add_argument('-v', '--verbosity', help='increase output verbosity',
#                     type=int, choices=[0, 1, 2])
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbosity == 2:
#     print(f'the square of {args.square} equals {answer}')
# elif args.verbosity == 1:
#     print(f'{args.square}^2 == {answer}')
# else:
#     print(answer)


# python  prog_05.py  4 -v 3
# usage: prog_05.py [-h] [-v {0,1,2}] square
# prog_05.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)

#  mamy zmianę w komunikacie o błędzie jak i w tekscie pomocy

# ---------------------------------------------------------------------

# inne podejście do verbosity
# jest liczona ilość wystąpień określonej opcji

# import argparse
# parser = argparse.ArgumentParser()
#
# parser.add_argument('square', type=int,
#                     help='display a square of a given number')
# parser.add_argument('-v', '--verbosity', action='count',
#                     help='increase output verbosity')
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbosity == 2:
#     print(f'the square of {args.square} equals {answer}')
# elif args.verbosity == 1:
#     print(f'{args.square}^2 == {answer}')
# else:
#     print(answer)

# python prog_05.py 4
# 16
# jeśli nie określimy flagi -v, to jej wartość ma None

# python prog_05.py 4 -v
# 4^2 == 16
# któtka postać flagi

# python prog_05.py 4 -vv
# the square of 4 equals 16
# przykład action='count'
# któtka postać flagi

# python prog_05.py 4 --verbosity
# 4^2 == 16
# długa postać flagi

# python prog_05.py 4 --verbosity --verbosity
# the square of 4 equals 16
# długa postać flagi


# python prog_05.py 4 -v 1
# usage: prog_05.py [-h] [-v] square
# prog_05.py: error: unrecognized arguments: 1

# python prog_05.py 4 -h
# usage: prog_05.py [-h] [-v] square
#
# positional arguments:
#   square           display a square of a given number
#
# options:
#   -h, --help       show this help message and exit
#   -v, --verbosity  increase output verbosity

# python prog_05.py 4 -vvv
# 16
# tu mamy błąd gdyż w skrypcie nie ma wystąpienia flagi -vvv

# action='count' zachwuje się podobnie jak action='store_true'

#  nasze wyniki pomocy nie zawierają informacji w temacie nowych możliwości
#  jakie uzyskał skrypt - to można naprawić, poprawiając dokumentację skrytpu
#  np. za pomocą argumentu słowa kluczowego help


# ---------------------------------------------------------------------

# wystąpienie flagi -vvv
# zastąpienie == >= usuwa błąd

# import argparse
# parser = argparse.ArgumentParser()
#
# parser.add_argument('square', type=int,
#                     help='display a square of a given number')
# parser.add_argument('-v', '--verbosity', action='count',
#                     help='increase output verbosity')
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbosity >= 2:
#     print(f'the square of {args.square} equals {answer}')
# elif args.verbosity >= 1:
#     print(f'{args.square}^2 == {answer}')
# else:
#     print(answer)


# python prog_05.py 4 -vvv
# the square of 4 equals 16
# args.verbosity = 3
# tu jest OK

# python prog_05.py 4 -vvvv
# the square of 4 equals 16
# args.verbosity = 4

# python prog_05.py 4
# Traceback (most recent call last):
#   File "/home/jazee/CODE/element_python/element/argparse/prog_05.py", line 175, in <module>
#     if args.verbosity >= 2:
# TypeError: '>=' not supported between instances of 'NoneType' and 'int'
#  tu jest nie OK

#  aby to poprawić należy wprowadzić wartość domyślną = 0

# ---------------------------------------------------------------------

# default = 0

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('square', type=int,
#                     help='display a square of a given number')
# parser.add_argument('-v', '--verbosity', action='count', default=0,
#                     help='increase output verbosity')
# args = parser.parse_args()
# answer = args.square ** 2
#
# if args.verbosity >= 2:
#     print(f'the square of {args.square} equals {answer}')
# elif args.verbosity >= 1:
#     print(f'{args.square}^2 == {answer}')
# else:
#     print(answer)

#  jeśli wartość default nie jest okreslona przymuje wartość None
# dlatego we wcześniejszym przykładzie wystąpił wyjątek TypeError

# python prog_05.py 4
# 16

# ---------------------------------------------------------------------
# Getting a little more advanced
# default = 0

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('x', type=int, help='the base')
# parser.add_argument('y', type=int, help='the exponent')
#
# parser.add_argument('-v', '--verbosity', action='count', default=0)
# args = parser.parse_args()
# answer = args.x ** args.y
#
# if args.verbosity >= 2:
#     print(f'{args.x} to the power {args.y} equals {answer}')
# elif args.verbosity >= 1:
#     print(f'{args.x}^{args.y} == {answer}')
# else:
#     print(answer)

# python prog_05.py
# usage: prog_05.py [-h] [-v] x y
# prog_05.py: error: the following arguments are required: x, y


# python prog_05.py -h
# usage: prog_05.py [-h] [-v] x y
#
# positional arguments:
#   x                the base
#   y                the exponent
#
# options:
#   -h, --help       show this help message and exit
#   -v, --verbosity


# python prog_05.py 4 2 -v
# 4^2 == 16


# ---------------------------------------------------------------------

# poziom stapnia szczegółowości

# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument('x', type=int, help='the base')
# parser.add_argument('y', type=int, help='the exponent')
#
# parser.add_argument('-v', '--verbosity', action='count', default=0)
# args = parser.parse_args()
# answer = args.x ** args.y
#
# if args.verbosity >= 2:
#     print(f"Running '{__file__}' ")
# if args.verbosity >= 1:
#     print(f'{args.x}^{args.y} == ', end='')
#
# print(answer)

# python prog_05.py 4 2
# 16

# python prog_05.py 4 2 -v
# 4^2 == 16

# python prog_05.py 4 2 -vv
# Running 'prog_05.py'
# 4^2 == 16

# -------------------------------------------------
# Conflicting options - konflikt opcji
# metoda add_mutually_exclusive_group() określić opcje, które kolidują ze sobą


# import argparse
#
# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-v', '--verbose', action='store_true')
# group.add_argument('-q', '--quiet', action='store_true')
#
# parser.add_argument('x', type=int, help='the base')
# parser.add_argument('y', type=int, help='the exponent')
#
# args = parser.parse_args()
# answer = args.x ** args.y
#
# if args.quiet:
#     print(answer)
# elif args.verbose:
#     print(f'{args.x} to the power {args.y} equals {answer}')
# else:
#     print(f'{args.x}^{args.y} == {answer}')

# python prog_05.py 4 2
# 4^2 == 16

# python prog_05.py 4 2 -q
# 16

# python prog_05.py 4 2 -v
# 4 to the power 2 equals 16

# python prog_05.py 4 2 -vq
# usage: prog_05.py [-h] [-v | -q] x y
# prog_05.py: error: argument -q/--quiet: not allowed with argument -v/--verbose
#
# nie możemy użyć obu flag na raz

# ------------------------------------------------
# informacja dla użytkowników jak jest cel programu



import argparse

parser = argparse.ArgumentParser(description='calculate X to the power of Y')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true')
group.add_argument('-q', '--quiet', action='store_true')

parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')

args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f'{args.x} to the power {args.y} equals {answer}')
else:
    print(f'{args.x}^{args.y} == {answer}')


# python prog_05.py -h
# usage: prog_05.py [-h] [-v | -q] x y
#
# calculate X to the power of Y
#
# positional arguments:
#   x              the base
#   y              the exponent
#
# options:
#   -h, --help     show this help message and exit
#   -v, --verbose
#   -q, --quiet


# https://docs.python.org/3.10/library/argparse.html#module-argparse
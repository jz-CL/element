# https://docs.python.org/3.10/howto/argparse.html#introducing-optional-arguments

# argumenty pocjonalne - 02

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--verbosity', help='increase output verbosity')
# args = parser.parse_args()
# if args.verbosity:
#     print('verbosity turned on')
#     print(args.verbosity)

# python prog_03.py --verbosity 0
# python prog_03.py --verbosity 1

# wartość args.verbosity -> 0 lub 1

# ---------------------------------------

#  aby przyjmować tylko True lub Falce

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--verbose', help='increase output verbosity',
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print('verbosity turned on')
    print(args.verbose)

#  python prog_03.py --verbose
# verbosity turned on
# True


# python prog_03.py --verbosity 1
# usage: prog_03.py [-h] [--verbosity]
# prog_03.py: error: unrecognized arguments: 1

#  opcja jest bardziej flagą niż czym co wymaga wartości

#  action="store_true" -> przypisuje wartość True do args.verbose

# python prog_03.py --help
#  mamy inny tekst pomocy
# usage: prog_03.py [-h] [--verbose]
#
# options:
#   -h, --help  show this help message and exit
#   --verbose   increase output verbosity



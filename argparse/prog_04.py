# Short options
# https://docs.python.org/3.10/howto/argparse.html#short-options

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help='increase output verbosity',
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print('verbosity turned on')
    print(args.verbose)

# python prog_04.py -v

# verbosity turned on
# True

# python prog_04.py --help
# usage: prog_04.py [-h] [-v]
#
# options:
#   -h, --help     show this help message and exit
#   -v, --verbose  increase output verbosity
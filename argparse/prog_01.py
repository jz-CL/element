# https://docs.python.org/3.10/howto/argparse.html#the-basics
import argparse

parser = argparse.ArgumentParser()
parser.parse_args()

# python prog_01.py
# uruchomienie bez aopcji nic nie robi -> nic nie wyświetla się na na stdout

# python prog_01.py --help
# usage: prog_01.py [-h]
#
# options:
#   -h, --help  show this help message and exit

# otrzymujemy wiadomość pomocy
# opcja --help / -h - jest jedyną opcją jaką otrzymujemy za free
# podanie czegokolwiek innego spowoduje błąd. Lecz również otrzymamy infomację dot.
# użytkowania


# --------------------------------------------

# python prog_01.py --verbose
# usage: prog_01.py [-h]
# prog_01.py: error: unrecognized arguments: --verbose

# --------------------------------------------

# python prog_01.py --foo
# usage: prog_01.py [-h]
# prog_01.py: error: unrecognized arguments: --foo

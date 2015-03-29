#!/usr/bin/env python3
__author__ = 'Dewep'


from hashcode.hashcode import HashCode
from sys import argv


hashcode = HashCode("final_round.in")

hashcode.score(argv[1] if len(argv) > 1 else "final_round.out")

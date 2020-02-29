#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    numToWords = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7:            'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13:               'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18:           'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23:        'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27:              'twenty seven', 28: 'twenty eight', 29: 'twenty nine', 30: 'thirty'}
    if m > 30:
        Hour = numToWords[h + 1]
    else:
        Hour = numToWords[h]

    if m == 0:
        return "{} o' clock".format(Hour)
    elif m == 1:
        return "one minute past {}".format(Hour)
    elif m > 1 and m < 15:
        return "{} minutes past {}".format(numToWords[m], Hour)
    elif m == 15:
        return "quarter past {}".format(Hour)
    elif m > 15 and m < 30:
        return "{} minutes past {}".format(numToWords[m], Hour)
    elif m == 30:
        return "half past {}".format(Hour)
    elif m > 30 and m < 45:
        m = 60 - m
        return "{} minutes to {}".format(numToWords[m], Hour)
    elif m == 45:
        return "quarter to {}".format(Hour)
    elif m > 45 and m < 59:
        m = 60 - m
        return "{} minutes to {}".format(numToWords[m], Hour)
    elif m == 59:
        m = 60 - m
        return "{} minute to {}".format(numToWords[m], Hour)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()


"""We search non-negative integer numbers, with at most 3 digits, such as the sum of the cubes of their digits
is the number itself; we will call them "cubic" numbers.

153 is such a "cubic" number : 1^3 + 5^3 + 3^3 = 153"""

from re import findall


def is_sum_of_cubes(s: str):
    numbers = findall("\d{1,3}", s)
    cubic = []
    for j in numbers:
        if int(j) == sum([i ** 3 for i in map(int, str(j))]):
            cubic.append(int(j))
    cubic.append(sum(cubic))
    if len(cubic) > 1:
        cubic.append("Lucky")
        return " ".join([str(x) for x in cubic])
    else:
        return "Unlucky"


### Best practice

import re

PATTERN = re.compile(r'(\d{1,3})')

def is_sum_of_cubes(s):
    found = list(filter(lambda nStr: int(nStr) == sum(int(d)**3 for d in nStr), PATTERN.findall(s)))
    return "Unlucky" if not found else "{} {} {}".format(' '.join(found), sum(map(int, found)), 'Lucky')




#!/usr/bin/env python3

# Author: Emmanuel Oyigoja Onah
# Author ID: 159610229
# Date Created: 2025/01/12

import sys

timer = 3

if len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer = timer - 1

print('blast off!')
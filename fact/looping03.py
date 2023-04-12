#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across range() to generate n UUIDs"""

import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

for rando in range(howmany):
    print( uuid.uuid4() )

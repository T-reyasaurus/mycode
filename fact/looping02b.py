#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        print(svr, end="")

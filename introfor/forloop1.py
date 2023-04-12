#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "Trey", "google"]

approved_vendors = ["cisco", "juniper", "arista"]


# loop across the list vendors
for vendor in vendors:
    print(f"Our vendor is {vendor}.")
    if vendor in approved_vendors:
        print("<= This is an approved vendor!", end="")

print("Our loop has completed.")


#!/usr/bin/env python3
"""Working with List"""

# values in list
my_list = ["192.168.0.5", 5060, "UP"]

# display the first, second, and last item in the list
print("The first item in the list (IP): " + my_list[0])
print("The second item in the list (port): " + str(my_list[1]))
print("The last item in the list (state): " + my_list[2])

# Challenge 01: given the list below display on the IP addresses on the screen
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
print(iplist[3:5])
# Even though the above function does display the ip addresses only, it was not part of the solutions given

# add up the strings
print("IP addresses: " + iplist[3] + ", and " +  iplist[4])

# use the comma separator
print("IP addresses: ", iplist[3],", and", iplist[4])

# use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")


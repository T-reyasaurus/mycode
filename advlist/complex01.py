#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print(list1)

    # display the first item in the list
    print(list1[1])

    # create a new list containing a single item
    list2 = ["juniper"]

    # extend list1 by list2
    list1.extend(list2)

    # display list1 with extend method
    print(list1)

    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

    # use the append operation to append list1 by list3
    list1.append(list3)

    # display list1 with append method of list3
    print(list1)

    # return the value of item 5 in list1
    print(list1[4])

    # print the first IP address
    print(list1[4][0])

    # create a list of 5 three letter animal names
    list4 = ["dog", "cat", "cow", "fox", "bat"]

    # display list4
    print(" ".join(list4).title())

main()


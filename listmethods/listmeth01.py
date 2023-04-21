#!/usr/bin/env python3

def main():
    proto = ["ssh", "http", "https"]
    protoa = ["ssh", "http", "https"]
    print(proto)

    # these lines will add "dns" to the end of the list above
    proto.append("dns")
    protoa.append("dns")
    # print proto to see the list method, append, take place on the list
    print(proto)
    
    # a list of common ports
    proto2 = [ 22, 80, 443, 53 ]
    # pass proto2 as an argument to the extend method
    proto.extend(proto2)

    print(proto)

    # pass proto2 as an argument to the append method
    protoa.append(proto2)
    print(protoa)

    # insert ftp at index 0 in proto
    print(len(proto)) # to see the lenght of index change before the insert takes place
    proto.insert(0, "ftp")
    print(proto)
    print(len(proto)) # to see the lenght of index change after the insert takes place

    # use the pop method to remove 'ftp' from proto
    proto.pop(0)
    print(proto)
    print(len(proto))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# create a list containing three items
#my_list = [ "192.168.0.5", 5060, "UP"]

# display the first item in the list
#print("The first item in the list (IP): " + my_list[0])

# display the second item in the list
#print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
#print("The last item in the list (state): " + my_list[2] )

#iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display on the IP addresses
#print("IP addresses: " + iplist[3] + ", and " + iplist[4])

#!/usr/bin/env python3
""" Alta3 Research | Lists Challenge """

# import random module
import random

def main():
    
    # enter variable data
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 
                  'Craig', 'Deja', 'Elihu', 'Eric', 
                  'Giovanni', 'James', 'Joshua', 'Maria', 
                  'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 
                  'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    # print the tlg list as shown above. This helps to compare differences later implemented.
    print(tlgstudents)
    
    # append the integer 4 to the wordbank list and then print the new list
    wordbank.append(4)
    print(wordbank)
    
    # for Bonus 2. Student name printed out below is related to input from user.
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]
    
    
    print(f"Your unfortunate victim is {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()


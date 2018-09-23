timestable = input("Enter the timestable you wish to learn (1-12) ")
# loop that will repeat 13 times (0-12)
for x in range(0,13):
    # the answer uses x which increases each time to work out the answer
    answer = x * int(timestable)
    # x is used in the print command to display what it is multiplying the number entered by
    print(timestable + " x " + str(x) + " = " + str(answer))

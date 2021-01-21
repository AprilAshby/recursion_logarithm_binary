# use this code in pythontutor to see how each step plays out:
# http://pythontutor.com/live.html#mode=edit

# My version
def print_number_range_april(x, y):
    if x <= y:
        print(x)
        print_number_range_april(x + 1, y)
    return


print_number_range_april(2, 6)


# Beej Jorgensen's version
def print_number_range_BeejJorgensen(x, y):
    # base case
    if x > y:
        return

    print("inbound:", x)
    print_number_range_BeejJorgensen(x+1, y)
    print("outbound:", x)
    return


print_number_range_BeejJorgensen(2, 6)

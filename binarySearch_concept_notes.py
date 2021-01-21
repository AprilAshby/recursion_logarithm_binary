# if list is unsorted we have to search the enitre list O(n)
# if you get unsorted data, is it worth spending the time to sort it so you can binary search?
# sorting takes O(o * log n) (worse than O(n))
# are you going to search repeatedly?
# then sort first

# sort first:
O(n log n) to sort
O(log n) to search
O(log n) to search
O(log n) to search
O(log n) to search
O(log n) to search

# dont sort:
O(n) to search
O(n) to search
O(n) to search
O(n) to search
O(n) to search
O(n) to search

# if it is sorted we can start in the middle and decide to look farther R or L.
# then repeat halving until we find it

# when you're throwing away half the data each iteration of your algorithm you have:
# O(log n) time complexity

binary_search(x, lst):
    comparing x to the middle number of the list
    if x is equal:
        return True
    if x > middle_number:
        binary_search(x, upper half of the lst)
    else:
        binary_search(x, lower half of the lst)

        # len()/2 might give you a decimal
        # len()//2 will give you an integer rounding down toward 0 each time

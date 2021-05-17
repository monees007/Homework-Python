def allindex(_char, _string):
    """
    The algorithm is:
    * Find index of the first occurrence of _char in _string
    * Split the string to discard the first occurrence along with all characters left to it.
    * For example: 'I have many elephant in my lunchbox'
        will result into ' many elephant in my lunchbox'
    * Repeat the above process to get other index.
    * But you will notice that, we will get [ 5 , 6 , 1 ]
        i.e. everytime indexing start from zeros
        so we will take cumulative form: [ 5 , 5+6 , 5+6+1 ]
    """
    l = [0]  # I can,t initiate with empty list because line 20 will read the last element of list
    for i in _string:
        if i == _char:
# ###############################################################################################################################################

            # Next line is adding one new element to list

            l = l + [l[-1] + _string.index(i)]

            # l[-1] is last item of list [ which is already sum of all previous index ]
            # _string.index(i) is index  of this occurrence

# ################################################################################################################################################

            # Next line is removing the read part of string

            _string = _string[_string.index(i) + 1:]

            ################################
# Next line is returning the list after removing the first list item [ the zero I added in line 13]
    return l[1:]


print(allindex('e', 'I have many elephant in my lunchbox'))


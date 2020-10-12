'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # i dont know how to account for the test count backwards 
    # TBC
    # internal iterator
    count = 0
    contains = "th" in word
    print(contains)
    print(word)
    # base case 0 th's
    if not contains:
        # return current count which is 0
        print("base case")
        return count
    else: # if not base case run function again
        # iterate count
        count += 1
        # remove one instance of th from function
        newWord = word.replace("th", "", 1)
        # run function again expecting count to iterate if there is more
        count += count_th(newWord)
    # at the end return the final count
    return count

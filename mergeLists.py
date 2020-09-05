# In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies
# orders and enter as one unit. Each order is represented by an "order id" (an integer). We have our lists of orders
# sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
#
# For example:
#   my_list     = [3, 4, 6, 10, 11, 15]
#   alices_list = [1, 5, 8, 12, 14, 19]
#
#   Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
#   print(merge_lists(my_list, alices_list))


a = [3, 4, 6, 10, 11, 15]
b = [1, 5, 8, 12, 14, 19]

def mergeLists(a,b):

    indexA = 0
    indexB = 0
    lengthA = len(a)
    lengthB = len(b)
    result = []

    while indexA < lengthA and indexB < lengthB:
        if a[indexA] < b[indexB]:
            result.append(a[indexA])
            indexA += 1
        else:
            result.append(b[indexB])
            indexB += 1

    if indexA != lengthA:
        while indexA < lengthA:
            result.append(a[indexA])
            indexA += 1

    if indexB != lengthB:
        while indexB < lengthB:
            result.append(b[indexB])
            indexB += 1

    return result

print(mergeLists(a,b))

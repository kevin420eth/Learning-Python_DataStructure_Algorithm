import math

def binarySearch(target_list, target):
    startIndex = 0
    endIndex = len(target_list)-1
    search_count = 0

    while startIndex <= endIndex:
        search_count += 1
        middleIndex = math.floor((startIndex+endIndex)/2)
        middleNumber = target_list[middleIndex]

        if middleNumber == target:
            return f'The target is in the array at index {middleIndex}\nSearch count: {search_count}'
        elif middleNumber > target:
            endIndex = middleIndex - 1
        else:
            startIndex = middleIndex + 1
    
    return f'The target is not in the array\nSearch count: {search_count}'

target_list = [1,2,3,4,5,6,7,8,9,10]

result = binarySearch(target_list,88)
print(result)

# ----------------------------Methodology----------------------------
#
# 1.Find the middle number of the list
# 2.Compare the middle number is the target number or not
# 3.If yes, then terminate the function, if no, change the startIndex or endIndex then keep running
# 4.Run the iteration until startIndex is equal to endIndex
#
# ----------------------------Analysis----------------------------
#
# The worst case of runtime is math.floor(log(n))+1
#
# Worst case may happen in both cases:
#   1.target is in the array
#   2.target is not in the array
#
# We can conclude that the worse-case time complexity of the binary search is O(log n) and 
# it's a efficient algorithm for searching an element in an ordered array
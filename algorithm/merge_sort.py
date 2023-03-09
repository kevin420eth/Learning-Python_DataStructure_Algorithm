def merge_sort(unsorted_list):
    if len(unsorted_list)==1:
        return unsorted_list
    
    mid_point = int(len(unsorted_list)/2)

    first_half = unsorted_list[:mid_point]
    second_half = unsorted_list[mid_point:]
    print(f'First half is {first_half}')
    print(f'Second half is {second_half}')
    half_a = merge_sort(first_half)
    half_b = merge_sort(second_half)

    return merge(half_a,half_b)

def merge(first_sublist,second_sublist):
    print(f'This is merging process for list {first_sublist} and {second_sublist}')
    i=j=0
    merged_list = []
    while i<len(first_sublist) and j<len(second_sublist):
        if first_sublist[i]<second_sublist[j]:
            merged_list.append(first_sublist[i])
            i+=1
        else:
            merged_list.append(second_sublist[j])
            j+=1

    while i<len(first_sublist):
        merged_list.append(first_sublist[i])
        i+=1

    while j<len(second_sublist):
        merged_list.append(second_sublist[j])
        j+=1
    
    print(merged_list)
    return merged_list

result = merge_sort([8,5,10,2,5,100,66,68,52,68,77])
print(result)

# ----------------------------Methodology----------------------------
# 1.Divide the given list into two equal sublist until each sublist only contains one element
# 2.Combine each sublist to a sorted order
#
# ----------------------------Analysis----------------------------
#

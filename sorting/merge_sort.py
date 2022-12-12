def merge_sub_arrys(list1, list2):
    '''Thsi function merges 2 sorted sub-arrays'''
    # initialize pointer & merged-sorted-sub-arrays
    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged


def divide(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        mylist[:mid] = divide(mylist[:mid])
        mylist[mid:] = divide(mylist[mid:])
        mylist = merge_sub_arrys(mylist[:mid], mylist[mid:])
    return mylist


if __name__ == '__main__':
    mylist = [6, 5, 12, 10, 9, 1]
    print(divide(mylist))

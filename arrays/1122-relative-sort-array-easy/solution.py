from collections import defaultdict


def relativeSortArray( arr1: list[int], arr2: list[int]) -> list[int]:
    arr2_set = set(arr2)
    arr1_count = defaultdict(int)
    no_show = []

    for num in arr1:
        if num not in arr2_set:
            no_show.append(num)
        arr1_count[num] += 1
    no_show.sort()

    print(arr1_count)
    # pp = pprint.PrettyPrinter(indent=4)
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])) # [2,2,2,1,4,3,3,9,6,7,19]

print(relativeSortArray([28,6,22,8,44,17], [22,28,8,6])) # [22,28,8,6,17,44]
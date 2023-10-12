#Binary  Search (CEIL AND FLOOR)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    floor, ceil = None, None
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
            floor = mid
        else:
            right = mid - 1
            ceil = mid
    return ceil,floor
arr = list(map(int,input().split()))
target = int(input())
result = binary_search(arr, target)
print(result)
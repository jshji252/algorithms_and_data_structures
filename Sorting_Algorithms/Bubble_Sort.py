nums = [1, 2, 3, 4, 8, 6, 9]

def bubble_sort(arr):
  for i in range(len(arr)):
    print(i)
    isSorted = True
    for idx in range(len(arr) - i - 1):
      if arr[idx] > arr[idx + 1]:
        isSorted = False
        # swap(arr, i, i + 1)
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    # if swapping didn't occur, we're good.
    if isSorted:
      break

print("PRE SORT: {0}".format(nums))
bubble_sort(nums)
print("POST SORT: {0}".format(nums))

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

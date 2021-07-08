from random import randrange, shuffle 
# IN-PLACE
def quicksort(list, start, end):
  # Base case
  if start >= end:
    return

  # Select pivot, randomly
  pivot_idx = randrange(start, end + 1)
  pivot_element = list[pivot_idx]

  # Move pivot elem to the end (will save some work, no computational benefir)
  list[end], list[pivot_idx] = list[pivot_idx], list[end]

  # The Less Than pointer
  less_than_pointer = start
  
  for i in range(start, end):
    # This is a LT. Move to the left.
    if list[i] < pivot_element:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # Move the LT pointer to the next position
      less_than_pointer += 1
  
  # Put back the pivot elem to the original location
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  # YAY! Now the list is [ *LessThans*, Pivot Elem, *GreaterThans* ]
  
  # Call quicksort on the "left" and "right" sub-lists
  # or, the "LeesThans" and "GreaterThans"
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)
  return None

# Not in place
def qs(arr):
  if len(arr) <= 1:
    return arr
 
  smaller = []
  larger = []
  
  pivot = 0
  pivot_element = arr[pivot]
  
  for i in range(1, len(arr)):
    if arr[i] > pivot_element:
      larger.append(arr[i])
    else:
      smaller.append(arr[i])
 
  sorted_smaller = qs(smaller)
  sorted_larger = qs(larger)
 
  return sorted_smaller + [pivot_element] + sorted_larger


unsorted_list = [3,7,12,24,36,42]
shuffle(unsorted_list)
unsort2 = unsorted_list.copy()
print(unsorted_list)
# use quicksort to sort the list, then print it out!
quicksort(unsorted_list, 0, len(unsorted_list)-1)
print(unsorted_list)
print(qs(unsort2))
# The two algs return the same result. In-place is more efficient due to less space complexity

# note: when a list is passed into a function, its reference is passed in. Thus working on 'list' modifies the original list
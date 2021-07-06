### Sorting

Sorting is important for a number of reasons. Binary search, for example, only works with a sorted set of data. There are many different sorting algorithms.

## Bubble Sort

The easiest and most straight forward sorting algorithm. When the data is already in a relatively sorted status, it can be useful. Notably, it requires very low space complexity of O(1) (constant).

1. Compare neighbouring values;
2. Repeat the following until sorted:
   1. If not in the order yet, swap
   2. If in order, move on

## Merge Sort

Using the _Divide and Conquer_ method, recurse until we reach the base case of a list with single element, then we merge. It's notable characteristic is that it has the same best, worst, average time complexity.

1. Check if the input list contains one element only (**base case**)
2. Split the list in half; left / right
3. Recurse the left/right to get left_sorted / right_sorted
4. Return merge(left_sorted, right_sorted)
5. Note the helper function merge()

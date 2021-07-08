### Sorting

Evidently, sorting is an important algorithm. Binary search, for example, only works with a sorted set of data. There are many different sorting algorithms, and here are a few most popular ones. Below is the summary of time / space complexity of the algorithms.

|             |     Worst Case      |  Average Case  | Best Case  | Space Complexity |
| :---------: | :-----------------: | :------------: | :--------: | :--------------: |
| Bubble Sort |       O(n^2)        |     O(n^2)     |    Ω(n)    |       O(1)       |
| Merge Sort  |     O(n log n)      |   O(n log n)   | Ω(n log n) |       O(n)       |
| Quick Sort  | O(n^2), technically | **O(n log n)** | Ω(n log n) |     O(log n)     |

Note that Quick Sort's worst case scenario is so uncommon, and can usually be avoided so it is safe to say it's big-O is O(n log n), rather than the worst case scenario of O(n^2)

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

## Quick Sort

Sorts quickly. Jks! What a name. Might as well name it, "great sort". Just kidding. Like Merge Sort, Quick Sort divides the list in half, so it also possesses the benefit of 'dividing'. Dividing is very desirable, because we can avoid a nested for loop. QS takes one step further in dividing process; everything on the left is _Less Than_ the **Pivot Value**, and everything on the right is _Greater Than_ the Pivot Value.

1. Check if the input list contains one or 0 element (**base case**)
2. Pick pivot wisely; _randomly_, for example.
3. Swap the last element and the pivot element (this will make our lives easier. also, we'll put it back later)
4. Declare a Less Than pointer at starting index.
5. Loop the entire list
   1. If a value is Less Than the pivot, move that element to where the pointer is
   2. Less Than Pointer += 1
6. Put back the pivot element to the origial position.
   - Notice now the list is in the following format:
   - [ *less than pivot elements* , PIVOT, *greater than pivot elements* ]
7. Repeat the same steps on the left (the less-thans) and on the right.

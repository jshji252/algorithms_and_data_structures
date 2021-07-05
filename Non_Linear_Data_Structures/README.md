### Binary Search Tree

## Basic

In Binary Search Tree (BST) structure, the smaller value is stored on the left child, and the bigger on the right child. Can have duplicate values if necessary. It is an efficient structure that can handle data retrieval / insertion with O(log N) time complexity.

## Traversal Techniques

The implemented algorithm uses _inorder_ traverse technique, which prints the left node value first, followed by the self, and the right node values. This is advantegeous in that it traverses the data in an ascending order. Other options include _preorder_, which traverses from self, followed by the left and the right nodes, and _postorder_, which traverses from the left, followed by the right, and self nodes.

### Min Heap

## Basic

We can visualise heap as a tree structure, however we simply store it in an array, while keeping track of indices. For min-heap, the min value will be kept at the root node, and **all children must be greater than their parents**.

## Addition

We add a new value to the end of the list, and then check if the addition violates the rule (children > parent). If so, we perform swapping until all obey the rule.

## Removal

When we remove the minimum value, we simply bring up the last element (the right-most element at the deepest level) to the top node, and check violation of rules.

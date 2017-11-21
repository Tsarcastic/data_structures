# Data-Structures




------------------
## Binary Search Tree
-------------------
The Binary Search Tree is a data structure used to sort numbers.

### Insert
The *insert(key, value)* method inserts a new Node into the tree. It will be sorted into its proper position relative to the other nodes. If the number is already in the tree the method will return an error.
The Time Complexity for this method could be O(N), but is more likely to be O(log N). This is because the tree could be lopsided forcing the method to iterate through each one.

### Contains
The *contains(val)* method returns True if the value is in the tree or False if it is not.
The Time Complexity for this method could be O(N), but is more likely to be O(log N). This is because the tree could be lopsided forcing the method to iterate through each one.

### Depth_side
The *depth_side(val, depth)* method checks to see if the node is being placed on the left or the right side of the tree. Then it adjusts the relevant depths and recalculates balance.
Time Complexity for size is O(1), since the values is tracked as an attribute.

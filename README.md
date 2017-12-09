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

### Balancing
The *balancing(parent)* method checks to see if the parent's parent node is balanced. If it's not it balances them.
Time Complexity for size is O(1), since the function does not depend on the size of the BST.

### Right_rotation, left_rotation, left_right, right_left
These methods rotate the nodes in the directions stated.
Time Complexity for size is O(1), since the time does not change based on the number of nodes.

### neo_depth_adjust
This method moves up from a child node and adjust the depth of its parents.
Time Complexity for size is O(log n), since it can at most move up one side of the tree.

### Restructure
This method will restructure nodes based on a node being deleted.
Time Complexity for size is O(log n), since the time changes based on the number of nodes but not at a 1 to 1 ratio.

### Delete
This will delete a node and restructure the BST to make sure it's balanced.
Time Complexity for size is O(log n), since it will at most traverse half the tree and it can also run the restructure function which takes O(log n)

------------------
## Trie
-------------------
The Trie is a data structure used to contain strings.

### Insert
This will insert a series of nodes into the tree that spell out the inserted word.
Time complexity for this is O(1).

### Contains
This will check to see if the Trie contains a word..
Time complexity for this is O(1), since the list of words is a dictionary at the starting node.

### Size
This will return the total number of words in the trie.
Time complexity for this is O(1).

### Size
If the word is in the trie this will remove it. If it doesn't it will return an error message.
Time complexity for this is O(1).


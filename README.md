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
## Sorts
-------------------
All sorts of sorts.

### Bubble Sort
This will compare an item to the one on its right, then if it's bigger the two will swap.
Time Complexity for size is O(N^2). This is because you may have to run through the sorting a shitton of times. (Scientific term)

### Merge Sort
This will divide the initial numbers into a series of sublists containing 1 number, then repeatedly merge sublists until there is only one sublist.
Time Complexity for size is (On log n). Since it will always split the lists into n sublists the time required is constant.

=======
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

------------------
## Autocomplete
-------------------
Autocomplete accepts two arguments when it is initialized.
1) A list of vocabulary words, which will be used to construct a trie as a property of the autocomplete object.
2) The maximum number of completions that will be provided when the object is later called. This defaults to 5.

When the autocomplete is called after instantiation it accepts one arguments.
This argument is the basis of the word being autocompleted.
Calling this object will return a list of possible completions for the word, 
    with the maximum size of the list being the second argument provided at instantiation.


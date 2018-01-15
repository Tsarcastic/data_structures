/*jshint esversion: 6 */
'use strict()'

class Node {
    constructor(key, value=null, left=null, right=null) {
        this.key = key
        if(value == null) {
            this.value = key
        } else {
            this.value = value
        }
        this.left = left 
        this.right = right
        this.parent = null
        this.left_depth = 0
        this.right_depth = 0
    }
}

class BST {
    constructor() {
        this.root = null
        this.size = 0
        this.list = []
    }

    insert(value, priority) {
        var new_node = new Node(value, priority)
        if(this.root == null) {
            this.root = new_node
            this.size += 1
        } else {
            var cur = this.root
            var completed = false
            while(completed == false) {
                if(new_node.value == cur.value) {
                    throw "That number is already in the tree."
                }

                this.size += 1

                if(new_node.value > cur.value) {
                    if(cur.right == null) {
                        cur.right = new_node
                        new_node.parent = cur
                        // this.depth_adjust(new_node)
                        completed = true
                    } else {
                        cur = cur.right
                    }
                } else {
                    if(cur.left == null) {
                        cur.left = new_node
                        new_node.parent = cur
                        //this.depth_adjust(new_node)
                        completed = true
                    } else {
                        cur = cur.left
                    }
                }
            }
        }
    }

    search(val) {
        var cur = this.root
        while (true == true) {
            if(cur.value == val) {
                return true
            } else if(val < cur.value) {
                if(cur.left != null) {
                    cur = cur.left
                } else {
                    return false
                }
            } else if(val > cur.value) {
                if(cur.right != null) {
                    cur = cur.right
                } else {
                    return false
                }
            }
        }
    }

    balancing(middle) {
        var top = middle.parent
        if(top != null) {
            var top_balance = top.right_depth - top.left_depth
            var middle_balance = middle.right_depth - middle.left_depth
            if(top_balance == -2) {
                if(middle_balance == -1) {
                    this.right_rotation(top)
                } else {
                    this.left_right(top)
                }
            } else {
                if(middle_balance == 1) {
                    this.left_rotation(top)
                } else {
                    this.right_left(top)
                }

            }
        }
    }

    right_rotation(root) {
        var pivot = root.left
        var base = root.parent
        pivot.parent = base
        
        if(pivot.parent == null) {
            this.root = pivot
        } else if(base.left == root) {
            base.left = pivot
        } else if(base.right == root) {
            base.right = pivot
        }

        root.left = pivot.right

        if(root.left != null) {
            root.left_depth = max(root.left.left_depth, root.left.right_depth) + 1
        } else {
            root.left_depth = 0
        }

        pivot.right = root
        pivot.right_depth = max(root.left_depth, root.right_depth) + 1
    }

    left_rotation(root) {
        var pivot = root.right
        var base = root.parent
        pivot.parent = root.parent
        if(pivot.parent == null) {
            this.root = pivot
        } else if(base.left == root) {
            base.left = pivot
        } else if(base.right == root) {
            base.right = pivot
        }

        root.parent = pivot
        root.right = pivot.left

        if(root.right != null) {
            root.right_depth = max(root.right.left_depth, root.right.right_depth) + 1
        } else {
            root.right_depth = 0
        }

        pivot.left = root
        pivot.left_depth = max(root.left_depth, root.right_depth) + 1

    }
}



module.exports = {Node, BST}
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

                if new_node.value > cur.value {
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

}
module.exports = {Node, Deque}
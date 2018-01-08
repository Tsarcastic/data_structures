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

class Deque {
    constructor() {
        this.head = null
        this.tail = null
        this._counter = 0
    }

}
module.exports = {Node, Deque}
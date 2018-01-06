/*jshint esversion: 6 */
'use strict()'

class Node {
    constructor(data, next=null) {
        this.data = data
        this.next = next
    }
}

class Stack {
    constructor() {
        this.head = null
        this._counter = 0
    }

    push(val) {
        this.head = new Node(val, this.head)
        this._counter += 1
    }

    pop() {
        if(this.head == null) {
            throw 'The stack is empty.'
        }
        var output = this.head.data
        this.head = this.head.next 
        this._counter += -1
        return output
    }
}

module.exports = {Node, Stack}
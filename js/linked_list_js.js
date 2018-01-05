'use strict'

class Node {
    constructor(data, next=null) {
        this.data = data
        this.next = next
    }
}


class LinkedList {
    constructor() {
        this.head = null
        this._counter = 0
    }

    size() {
        return this._counter
    }

    push(val) {
        this.head = new Node(val, this.head)
        this._counter += 1
    }
}
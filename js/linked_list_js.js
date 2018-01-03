'use strict'

class Node {
    constructor(data) {
        this.data = data
        this.next = null
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

    
}
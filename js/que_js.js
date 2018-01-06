/*jshint esversion: 6 */
'use strict()'

class Node {
    constructor(data, previous) {
        this.data = data
        this.previous = previous
        this.next = null
    }
}

class Queue {
    constructor() {
        this.head = null
        this.tail = null
        this._counter = 0
    }

    size() {
        return this._counter
    }

    enqueue(val) {
        var new_tail = new Node(val, self.tail)
        if(this.tail == null) {
            this.tail = new_tail
            this.head = new_tail
        }
        else {
            this.tail.next = new_tail
            this.tail = new_tail
        }
        this._counter += 1
    }

    dequeue() {
        if(this.head == null) {
            throw 'The queue is empty.'
        }
        this._counter += -1
        var output = this.head.data
        if(this.head.next != null) {
            this.head.next.previous = null
            this.head = this.head.next
        }
        else {
            this.head = null
            this.tail = null
        }
        return output
    }

    peek() {
        return this.head.data
    }


}

module.exports = {Node, Queue}
/*jshint esversion: 6 */
'use strict()'

class Node {
    constructor(data, next=null, previous=null) {
        this.data = data
        this.next = next
        this.previous = previous
    }
}
class Deque {
    constructor() {
        this.head = null
        this.tail = null
        this._counter = 0
    }

    size() {
        return this._counter
    }

    append_head(val) {
        var new_head = new Node(val, this.head)
        if(this.head == null) {
            this.head = new_head
            this.tail = new_head
        }
        else {
            this.head.previous = new_head
            this.head = new_head
        }
        this._counter += 1
    }

    append_tail(val) {
        var new_tail = new Node(val, null, this.tail)
        if(this.tail == null) {
            this.head = new_tail
            this.tail = new_tail
        }
        else {
            this.tail.next = new_tail
            this.tail = new_tail
        }
        this._counter += 1
    }

    pop_head() {
        if(this.head == null) {
            throw 'The deque is empty.'
        }
        else if(this.head == this.tail) {
            this._counter += -1
            var output = this.head.data
            this.head = null
            this.tail = null
            return output
        }
        else {
            this._counter += -1
            var temp = this.head.data
            this.head.next.previous = null
            this.head = this.head.next
            return temp
        }
    }

    pop_tail() {
        if(this.tail == null) {
            throw 'The deque is empty.'            
        }
        else if(this.head == this.tail) {
            this._counter += -1
            var output = this.tail.data
            this.head = null
            this.tail = null
            return output
        }
        else {
            this._counter += -1
            var temp = this.tail.data
            this.tail.previous.next = null
            this.tail = this.tail.previous
            return temp
        }       

    }

    peek_tail() {
        if(this.tail == null) {
            throw 'The deque is empty.'            
        }
        else {
            return this.tail.data
        }
    }

    peek_head() {
        if(this.head == null) {
            throw 'The deque is empty.'            
        }
        else {
            return this.head.data
        }
    }
}


module.exports = {Node, Deque}
/*jshint esversion: 6 */
'use strict()'

class Node {
    constructor(data, next, previous=null) {
        this.data = data
        this.next = next
        this.previous = previous
    }
}

class DoubleLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this._counter = 0
    }

    size() {
        return this._counter
    }

    push_head(val) {
        var new_head = new Node(val, this.head)
        this._counter += 1
        if(this.head == null) {
            this.tail = new_head
            this.head = new_head
        }
        else {
            this.head.previous = new_head
            this.head= new_head
        }
    }

    push_tail(val) {
        var new_tail = new Node(val, null, this.tail)
        this._counter += 1
        if(this.tail == null) {
            this.tail = new_tail
            this.head = new_tail
        }
        else {
            this.tail.next = new_tail
            this.tail = new_tail
        }
    }

    pop_head() {
        if(this.head == null) {
            throw 'This list is empty.'
        } else if(this.head == this.tail) {
            var output = this.head.data
            this.head = null
            this.tail = null
            this._counter --
            return output
        } else {
            var temp = this.head.data
            this.head = this.head.next
            this.head.previous = null
            this._counter --
            return temp
        }
    }

    pop_tail() {
        if(this.tail == null) {
            throw 'This list is empty.'
        } else if(this.head == this.tail) {
            var output = this.tail.data
            this.head = null
            this.tail = null
            this._counter --
            return output
        } else {
            var temp = this.tail.data
            this.tail = this.tail.previous
            this.tail.next = null
            this._counter --
            return temp
        }
    }

    remove(val) {
        var curr = this.head
        if(curr == null) {
            throw 'The list is empty.'
        } else if((this.head == this.tail) && (this.head.data == val)) {
            this.head = null
            this.tail = null
            this._counter --
            console.log('That item has been removed. This list is now empty.')
            return
        } else if(this.head.data == val) {
            this.head = this.head.next
            this.head.previous = null
            this._counter --
            console.log('The head has been removed.')
            return
        } else if(this.tail.data == val) {
            this.tail = this.tail.previous
            this.tail.next = null
            this._counter --
            console.log('The tail has been removed')
            return
        } else {
        while (curr.next != null) {
            if(curr.next.data == val) {
                curr.next = curr.next.next
                this._counter += -1
                console.log('The item has been removed')
                return
            }
            curr = curr.next
        }
        return false
        }
    }
}

module.exports = {Node, DoubleLinkedList}
/*jshint esversion: 6 */
'use strict()'


var sum = require('./sum')

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

    pop() {
        if(this.head == null) {
        }
        var output = this.head.data
        this.head = this.head.next 
        this._counter += -1
        return output
    }

    search(val) {
        var curr = this.head 
        if(curr === null) {
            throw 'The list is empty.'
        }
        while (curr != null) {
            if (curr.data == val) {
                return true
            }
            curr = curr.next
        }
        

    }

    remove(val) {
        var curr = this.head
        if(curr == null) {
            throw 'The list is empty.'
        }
        while (curr != null) {
            if(curr.next.data == val) {
                curr.next = curr.next.next
                self._counter += -1
                return
            }
            curr = curr.next
        }


    }

    display() {
        if (self._counter == 0) {
            throw 'The list is empty.'
        }
        var curr = this.head
        var the_answer = []
        while (curr != null) {
            the_answer.push(curr.data)
            curr = curr.next
        }
        return the_answer.join(',')
    }

}

module.exports = {LinkedList, Node}
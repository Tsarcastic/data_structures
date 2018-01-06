/*jshint esversion: 6 */
'use strict()'

class Binheap {
   constructor(iterable=[]) {
        this.bin_list = [0]
        this.heap_index = 0
        if(iterable.length > 0) {
            for (var i = 0; i < iterable.length; i++) {
                this.push_list(iterable[i])
            }
        }
    }

    display() {
        console.log(this.heap_index.toString())
    }

    push_list(val) {
        this.bin_list.push(val)
        this.heap_index += 1
        this.sort_up(this.heap_index)
    }

    sort_up(index) {
        var range = this.heap_index
        while(range > 0) {
            if(this.bin_list[index] < this.bin_list[Math.floor(index / 2)]) {
                var temp = this.bin_list[Math.floor(index / 2)]
                this.bin_list[Math.floor(index / 2)] = this.bin_list[index]
                this.bin_list[index] = temp
                index = Math.floor(index / 2)
            }
            range += -1
        }
    }

    sort_down() {
        var index = 1
        while(index * 2 <= this.heap_index) {
            var child_idx = index * 2
            if((index * 2) + 1 <= this.heap_index) {
                if(this.bin_list[index * 2] > this.bin_list[(index * 2) + 1]) {
                    child_idx = (index * 2) + 1
                } else {
                    child_idx = index * 2
                }
            } else {
                child_idx = index * 2
            }
            var parent = this.bin_list[index]
            if(this.bin_list[index] > this.bin_list[child_idx]) {
                this.bin_list[index] = this.bin_list[child_idx]
                this.bin_list[child_idx] = parent
            }
            index = child_idx
        }
    }

    pop() {
        if(this.heap_index == 0) {
            throw 'The binary heap is empty.'
        }
        var to_remove = this.bin_list[1]
        this.bin_list[1] = this.bin_list[this.bin_list.length -1]
        this.bin_list = this.bin_list.slice(0, -1)
        this.heap_index += -1
        this.sort_down()
        return to_remove
    }
}

module.exports = {Binheap}











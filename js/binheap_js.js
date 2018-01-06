/*jshint esversion: 6 */
'use strict()'

class Binheap {
    constructor() {
        this.bin_list = [0]
        this.heap_index = 0
    }

    display() {
        console.log(this.heap_index.toString())
    }

    push(val) {
        this.bin_list.append(val)
        this.heap_index += 1
        this.sort(this.heap_index)
    }

    sort_up(index) {
        var range = this.heap_index
        while(range > 0) {
            if(this.bin_list[index] < this.bin_list[floor(index / 2)]) {
                var temp = this.bin_list[floor(index / 2)]
                this.bin_list[floor(index / 2)] = this.bin_list[index]
                this.bin_list[index] = temp
                index = floor(index / 2)
            }
            range += -1
        } 
    }
}
















module.exports = Binheap











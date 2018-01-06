/*jshint esversion: 6 */
'use strict()'

var new_heap = require('../binheap_js')

test('Structure works', () => {
    var test_heap = new new_heap.Binheap()
    expect(test_heap.heap_index).toEqual(0)
    expect(test_heap.bin_list).toEqual([0])    
})

test('Push_list works', () => {
    var test_heap = new new_heap.Binheap()
    test_heap.push_list(5)
    test_heap.push_list(10)
    expect(test_heap.heap_index).toEqual(2)
    expect(test_heap.bin_list).toEqual([0, 5, 10])    
})

test('Iterable constructor works', () => {
    var test_heap = new new_heap.Binheap([5, 10])
    expect(test_heap.heap_index).toEqual(2)
    expect(test_heap.bin_list).toEqual([0, 5, 10])    
})

test('Popping is working as intended.', () => {
    var test_heap = new new_heap.Binheap([5, 10, 3])
    expect(test_heap.bin_list).toEqual([0, 3, 10, 5])
    expect(test_heap.pop()).toBe(3)
    expect(test_heap.bin_list).toEqual([0, 5, 10])    
    expect(test_heap.pop()).toBe(5)
    expect(test_heap.pop()).toBe(10)
    expect(test_heap.bin_list).toEqual([0])    
})

test('Correct structure with appens', () => {
    var test_heap = new new_heap.Binheap([7, 14, 5, 1, 6, 8])
    expect(test_heap.bin_list).toEqual([0, 1, 5, 7, 14, 6, 8])
})

test('Returns values in ascending order', () => {
    var test_heap = new new_heap.Binheap([7, 14, 5, 1, 6, 8])
    expect(test_heap.pop()).toBe(1)
    expect(test_heap.pop()).toBe(5)
    expect(test_heap.pop()).toBe(6)
    expect(test_heap.pop()).toBe(7)
    expect(test_heap.pop()).toBe(8)
    expect(test_heap.pop()).toBe(14)    
})

test('Pushes and pops work together 01', () => {
    var test_heap = new new_heap.Binheap([5, 19, 33, 1, 3])
    expect(test_heap.bin_list).toEqual([0, 1, 3, 33, 19, 5])
})

test('Pushes and pops work together 02', () => {
    var test_heap = new new_heap.Binheap([5, 19, 33, 1, 3])
    expect(test_heap.pop()).toBe(1)
    test_heap.push_list(2)
    expect(test_heap.bin_list).toEqual([0, 2, 3, 33, 19, 5])
})

test('Pushes and pops work together 03', () => {
    var test_heap = new new_heap.Binheap([5, 19, 33, 1, 3])
    expect(test_heap.pop()).toBe(1)
    test_heap.push_list(2)
    test_heap.push_list(44)
    expect(test_heap.bin_list).toEqual([0, 2, 3, 33, 19, 5, 44])
})

test('Pushes and pops work together 04', () => {
    var test_heap = new new_heap.Binheap([5, 19, 33, 1, 3])
    expect(test_heap.pop()).toBe(1)
    test_heap.push_list(2)
    test_heap.push_list(44)
    expect(test_heap.bin_list).toEqual([0, 2, 3, 33, 19, 5, 44])
})

test('Pushes and pops work together 05', () => {
    var test_heap = new new_heap.Binheap([5, 19, 33, 1, 3])
    expect(test_heap.pop()).toBe(1)
    test_heap.push_list(2)
    test_heap.push_list(44)
    expect(test_heap.pop()).toBe(2)
    test_heap.push_list(4)    
    expect(test_heap.bin_list).toEqual([0, 3, 5, 4, 19, 44, 33])
})

test('Always returns lowest', () => {
    var output = []
    var test_heap = new new_heap.Binheap([1, 17, 9, 13, 33, 2, 19, 16, 53, 3, 4, 99])
    while(test_heap.bin_list.length > 1) {
        output.push(test_heap.pop())
    }
    expect(output).toEqual([1, 2, 3, 4, 9, 13, 16, 17, 19, 33, 53, 99])
})
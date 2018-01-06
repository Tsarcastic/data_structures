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
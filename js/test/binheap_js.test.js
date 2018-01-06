/*jshint esversion: 6 */
'use strict()'

var new_heap = require('../binheap_js')

test('Structure works', () => {
    var test_heap = new new_heap.Binheape()
    expect(test_heap.list_index).toBe(0)
    expect(test_heap.bin_list).toBe([0])    
})
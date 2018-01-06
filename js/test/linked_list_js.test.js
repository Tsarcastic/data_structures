/*jshint esversion: 6 */
'use strict()'

var ll = require('../linked_list_js')

//test('adds 1 + 2 to equal 3', () => {
 // expect(sum(1, 2)).toBe(3);
// });

test('Node works', () => {
    var test_node = new ll.Node(5)
    expect(test_node.data).toBe(5)
})
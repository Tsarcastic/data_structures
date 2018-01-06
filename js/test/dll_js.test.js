/*jshint esversion: 6 */
'use strict()'

var js_dll = require('../dll_js')

test('Node works', () => {
    var test_node = new js_dll.Node(5)
    expect(test_node.data).toBe(5)
})

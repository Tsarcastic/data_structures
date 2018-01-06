/*jshint esversion: 6 */
'use strict()'

var js_stack = require('../stack_js.js')

test('Node works', () => {
    var test_node = new js_stack.Node(5)
    expect(test_node.data).toBe(5)
})

test('Node works', () => {
    var test_node = new js_stack.Node(5)
    expect(test_node.data).toBe(5)
})

test('Stack has null head', () => {
    var test_stack = new js_stack.Stack()
    expect(test_stack.head).toBe(null)
})

test('Stack push adds new nodes', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push('val')
    expect(test_stack.head.data).toBe('val')
})

test('Pushing 2 values to stack works', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push(3)
    test_stack.push(7)
    expect(test_stack.head.data).toBe(7)
})

test('Moves old head to next', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push(3)
    test_stack.push(5)
    expect(test_stack.head.next.data).toBe(3)
})

test('Pop removes head', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push(3)
    test_stack.pop()
    expect(test_stack.head).toBeNull()
})

test('Pop returns head value', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push(3)
    test_stack.push(5)
    expect(test_stack.pop()).toBe(5)
})

test('Pop shifts head', () => {
    var test_stack = new js_stack.Stack()
    test_stack.push(3)
    test_stack.push(5)
    test_stack.pop()
    expect(test_stack.pop()).toBe(3)
})
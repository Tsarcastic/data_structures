/*jshint esversion: 6 */
'use strict()'

var js_deque = require('../deque_js')

test('Node works', () => {
    var test_node = new js_deque.Node(5)
    expect(test_node.data).toBe(5)
})

test('Deque has null head', () => {
    var test_deque = new js_deque.Deque()
    expect(test_deque.head).toBe(null)
})

test('Append_head adds new nodes', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_head('val')
    expect(test_deque.head.data).toBe('val')
    expect(test_deque.tail.data).toBe('val')
})

test('Append_tail adds new nodes', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_tail('val')
    expect(test_deque.head.data).toBe('val')
    expect(test_deque.tail.data).toBe('val')
})

test('Appending moves head.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_head(2)
    test_deque.append_head(5)
    expect(test_deque.head.data).toBe(5)
    expect(test_deque.tail.data).toBe(2)
    expect(test_deque.head.next.data).toBe(2)
})

test('Appending moves tail.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_tail(2)
    test_deque.append_tail(5)
    expect(test_deque.head.data).toBe(2)
    expect(test_deque.tail.data).toBe(5)
    expect(test_deque.tail.previous.data).toBe(2)
})

test('Pop_head maintains the structure.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_head(2)
    test_deque.append_head(5)
    test_deque.append_head(17)
    expect(test_deque.pop_head()).toBe(17)
    expect(test_deque.head.data).toBe(5)
    expect(test_deque.tail.data).toBe(2)
    expect(test_deque.tail.previous.data).toBe(5)
    expect(test_deque.head.next.data).toBe(2)
})

test('Pop_head works fine with one.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_head(2)
    expect(test_deque.pop_head()).toBe(2)
    expect(test_deque.head).toBeNull()
    expect(test_deque.tail).toBeNull()
})

test('Pop_tail maintains the structure.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_tail(2)
    test_deque.append_tail(5)
    test_deque.append_tail(17)
    expect(test_deque.pop_tail()).toBe(17)
    expect(test_deque.tail.data).toBe(5)
    expect(test_deque.head.data).toBe(2)
    expect(test_deque.head.next.data).toBe(5)
    expect(test_deque.tail.previous.data).toBe(2)
    expect(test_deque.size()).toBe(2)
})

test('Pop_tail works fine with one.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_head(2)
    expect(test_deque.pop_tail()).toBe(2)
    expect(test_deque.head).toBeNull()
    expect(test_deque.tail).toBeNull()
    expect(test_deque.size()).toBe(0)    
})

test('Peeking works.', () => {
    var test_deque = new js_deque.Deque()
    test_deque.append_tail(2)
    test_deque.append_tail(5)
    expect(test_deque.peek_head()).toBe(2)
    expect(test_deque.peek_tail()).toBe(5)
})
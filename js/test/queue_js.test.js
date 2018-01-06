/*jshint esversion: 6 */
'use strict()'

var js_que = require('../que_js')

test('Node works', () => {
    var test_node = new js_que.Node(5)
    expect(test_node.data).toBe(5)
})

test('Queue has null head', () => {
    var test_queue = new js_que.Queue()
    expect(test_queue.head).toBe(null)
})

test('Queue enqueue adds new nodes', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue('val')
    expect(test_queue.head.data).toBe('val')
})

test('Pushing 2 values to queue works', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(7)
    expect(test_queue.head.data).toBe(3)
})

test('Old nodes are moved to the tail.', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(5)
    expect(test_queue.head.next.data).toBe(5)
})

test('The tail changes.', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(5)
    expect(test_queue.tail.data).toBe(5)
})

test('Dequeue removes head', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.dequeue()
    expect(test_queue.head).toBeNull()
})

test('Dequeue returns head value', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(5)
    expect(test_queue.dequeue()).toBe(3)
})

test('Dequeue shifts head', () => {
    var test_queue = new js_que.Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(5)
    test_queue.dequeue()
    expect(test_queue.peek()).toBe(5)
})
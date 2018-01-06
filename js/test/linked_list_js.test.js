/*jshint esversion: 6 */
'use strict()'

var ll = require('../linked_list_js')

test('Node works', () => {
    var test_node = new ll.Node(5)
    expect(test_node.data).toBe(5)
})

test('Linked List has null head', () => {
    var test_list = new ll.LinkedList()
    expect(test_list.head).toBe(null)
})

test('Linked List push adds new nodes', () => {
    var test_list = new ll.LinkedList()
    test_list.push('val')
    expect(test_list.head.data).toBe('val')
})

test('Pushing 2 values to ll works', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(7)
    expect(test_list.head.data).toBe(7)
})

test('Moves old head to next', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    expect(test_list.head.next.data).toBe(3)
})

test('Pop removes head', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.pop()
    expect(test_list.head).toBeNull()
})

test('Pop returns head value', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    expect(test_list.pop()).toBe(5)
})

test('Pop shifts head', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    test_list.pop()
    expect(test_list.pop()).toBe(3)
})

test('Size works correctly.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    expect(test_list.size()).toBe(2)
})

test('Size works correctly - 2.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    test_list.pop()
    expect(test_list.size()).toBe(1)
})

test('Basic search works.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    expect(test_list.search(3)).toBe(true)
})

test('Search will fail.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    expect(test_list.search(1)).toBe(false)
})

test('Remove works.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    test_list.remove(5)
    expect(test_list.search(5)).toBe(false)
})

test('Remove works.', () => {
    var test_list = new ll.LinkedList()
    test_list.push(3)
    test_list.push(5)
    test_list.remove(5)
    expect(test_list.search(5)).toBe(false)
})
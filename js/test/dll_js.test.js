/*jshint esversion: 6 */
'use strict()'

var js_dll = require('../dll_js')

test('Node works', () => {
    var test_node = new js_dll.Node(5)
    expect(test_node.data).toBe(5)
})

test('Node exists in continuum 01', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    expect(test_dll.head.next.previous.data).toBe('orange')
})

test('Node exists in continuum 02', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    expect(test_dll.head.next.data).toBe('banana')
})

test('Node exists in continuum 03', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    expect(test_dll.head.next.next).toBe(null)
})

test('Pop off 01', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    expect(test_dll.pop_tail()).toBe('banana')
})

test('Pop off 02', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    test_dll.pop_head()
    expect(test_dll.head == test_dll.tail)
})

test('Pop tail changes length', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    test_dll.pop_head()
    expect(test_dll.size()).toEqual(1)
})

test('Pop tail changes tail', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    test_dll.pop_tail()
    expect(test_dll.head.data).toBe('orange')
})

test('Pop tail changes tail', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    test_dll.push_head('orange')
    test_dll.pop_tail()
    expect(test_dll.head == test_dll.tail)
})

test('Push tail on empty list', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_tail('banana')
    expect(test_dll.head.data).toBe('banana')
})

test('Push head increments counter', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('banana')
    expect(test_dll.size()).toEqual(1)
})

test('Tail and head are related', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_tail('blue')
    test_dll.push_tail('red')
    expect(test_dll.head.next.data).toBe('red')
})

test('Popping a list empty removes head and tail.', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('red')
    test_dll.pop_tail()
    expect(test_dll.head).toBe(null)
})

test('Remove works', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('z')
    test_dll.push_head('x')
    test_dll.push_head('y')
    test_dll.remove('x')
    expect(test_dll.head.next.data).toBe('z')
})

test('Remove works fine if head is tail', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('x')
    test_dll.remove('x')
    expect(test_dll.head).toBe(null)
})

test('Removing an item that doesnt exist returns false', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('z')
    expect(test_dll.remove('x')).toBe(false)
})

test('Removing a tail is fine', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('z')
    test_dll.push_tail('x')
    expect(test_dll.tail.previous.data).toBe('z')
    expect(test_dll.tail.data).toBe('x')    
    test_dll.remove('x')
    expect(test_dll.tail.data).toBe('z')
})

test('Removing a head is fine', () => {
    var test_dll = new js_dll.DoubleLinkedList()
    test_dll.push_head('z')
    test_dll.push_tail('x')   
    test_dll.remove('z')
    expect(test_dll.head.data).toBe('x')
})
/*jshint esversion: 6 */
'use strict()'

var js_graph = require('../graph_js.js')

test('Structure works', () => {
    var test_graph = new js_graph.Graph()  
    expect(test_graph.node_list).toEqual([])
    expect(test_graph.edges).toEqual({})
})

test('Add_node() populates graph', () => {
    var test_graph = new js_graph.Graph() 
    test_graph.add_node(1) 
    expect(test_graph.node_list[0]).toEqual(1)
    expect(test_graph.edges).toEqual({})
})

test('Nodes() works', () => {
    var test_graph = populated_graph() 
    expect(test_graph.nodes()).toEqual([1, 2, 3, 4])
    expect(test_graph.edges).toEqual({})
})

test('Add_edge() works', () => {
    var test_graph = populated_graph() 
    test_graph.add_edge(5, 6)
    expect(test_graph.edges).toEqual({"5,6": 0})
})

test('Del_node() works', () => {
    var test_graph = populated_edges_graph() 
    test_graph.del_node(1)
    expect(test_graph.node_list).toEqual([2, 3, 4])
    expect(test_graph.edges).toEqual({"3,2": 0, "4,1": 0})    
})


function populated_graph() {
    test_graph = new js_graph.Graph()
    test_graph.add_node(1)
    test_graph.add_node(2)
    test_graph.add_node(3)
    test_graph.add_node(4)
    return test_graph    
}

function populated_edges_graph() {
    test_graph.add_edge(1, 2)
    test_graph.add_edge(1, 4)
    test_graph.add_edge(3, 2)
    test_graph.add_edge(4, 1)
    return test_graph
}
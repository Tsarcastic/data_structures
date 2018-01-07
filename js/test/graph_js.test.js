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

test('Populated_edges function works', () => {
    var test_edge_graph = populated_edges_graph() 
    expect(test_edge_graph.node_list).toEqual([1, 2, 4, 3])
    expect(test_edge_graph.edges).toEqual({"1,2": 0, "1,4": 0,"3,2": 0, "4,1": 0})    
})

test('del_node() modifies the node list and edge list appropriately', () => {
    var test_graph = populated_edges_graph()
    expect(test_graph.edges).toEqual({"1,2": 0, "1,4": 0,"3,2": 0, "4,1": 0}) 
    test_graph.del_node(1)
    expect(test_graph.node_list).toEqual([2, 4, 3])
    //expect(test_graph.edges).toEqual({"3,2": 0, "4,1": 0})    
})

test('has_node() works', () => {
    var test_graph = populated_graph() 
    expect(test_graph.has_node(1)).toEqual(true)
})

test('neighbors() works', () => {
    var test_graph = populated_edges_graph() 
    expect(test_graph.neighbors(1)).toEqual([2, 4])
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
    test_graph = new js_graph.Graph()
    test_graph.add_edge(1, 2)
    test_graph.add_edge(1, 4)
    test_graph.add_edge(3, 2)
    test_graph.add_edge(4, 1)
    return test_graph    
}
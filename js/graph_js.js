/*jshint esversion: 6 */
'use strict()'

class Graph {
    constructor() {
        this.node_list = []
        this.edges = {}
    }

    nodes() {
        return this.node_list
    }

    edge_report() {
        return Object.keys(edges)
    }

    add_node(val) {
        this.node_list.push(val)
    }

    add_edge(val1, val2, wt=0) {
        if (!((val1) in node_list)) {
            this.add_node(val1)
        }
        if (!((val2) in node_list)) {
            this.add_node(val2)
        }
        this.edges[(val1, val2)] = wt
    }

    del_node(val) {
        var temp_edges = {}
        if(val in this.node_list) {
            delete this.node_list[val]
            for(var key in this.edges) {
                if (!(val in key)) {
                    temp_edges[key] = this.edges[key]
                }
            this.edges = temp_edges
            }
        }
    }

    has_node(val) {
        return (val in self.node_list)
    }

    neighbors(val) {
        var temp_list = []
        for(var key in this.edges) {
            if(val in key) {
                if(val == key[0]) {
                    temp_list.push(key[1])
                }
                else {
                    temp_list.push(key[0])
                }
            }
        }
    }

    adjacent(val1, val2) {
        if((val1, val2) in this.edges) {
            return true
        }
        else if((val1 in self.node_list) || (val2 in self.node_list)) {
            return false
        }
        else {
            throw 'Neither of those are in the graph.'
        }
    }


}
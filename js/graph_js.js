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
        return Object.keys(this.edges)
    }

    add_node(val) {
        this.node_list.push(val)
    }

    add_edge(val1, val2, wt=0) {
        if (!(this.node_list.includes(val1))) {
            this.add_node(val1)
        }
        if (!(this.node_list.includes(val2))) {
            this.add_node(val2)
        }
        this.edges[String(val1) + "," + String(val2)] = wt
    }
    //del node needs a lot of work. messes up values in dict and doesn't remove associated edges
    del_node(val) {
        var temp_edges = {}
        if(this.node_list.includes(val)) {
            var temp_index = this.node_list.indexOf[val]
            this.node_list.splice(temp_index, 1)
            
            for(var key in this.edges) {
                var array_key = key.split(",")
                if (!(array_key.includes(val))) {
                    temp_edges[key] = this.edges[key]
                }
            this.edges = temp_edges
            }
        }
    }

    has_node(val) {
        return (val in this.node_list)
    }

    neighbors(val) {
        var temp_list = []
        for(var key in this.edges) {
            var array_key = key.split(",")
            //temp_list.push(array_key)
            for(var sub_item in array_key) {
                temp_list.push(sub_item[0])
                /*if(sub_item[0] == val) {
                    temp_list.push(array_key[1])
                }
                if(sub_item[1] == val) {
                    temp_list.push(array_key[0])
                } */
            }
        }
        /*var set = new Set(temp_list)
        temp_list = []
        for(var item in set) {
            temp_list.push(item)
        } */
        return temp_list
    }

    adjacent(val1, val2) {
        if((val1, val2) in this.edges) {
            return true
        }
        else if((val1 in this.node_list) || (val2 in this.node_list)) {
            return false
        }
        else {
            throw 'Neither of those are in the graph.'
        }
    } 
}

function convert_string_to_tuple(string) {
    var output = string.split(",")
}

module.exports = {Graph}
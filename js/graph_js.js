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
    //del node doesn't remove associated edges
    del_node(val) {
        var temp_edges = {}
        if(this.node_list.includes(val)) {
            var temp_index = this.node_list.indexOf[val]
            if (temp_index != -1) {
                this.node_list = this.node_list.slice(temp_index, temp_index)
            }
            
            for(var key in this.edges) {
                var array_key = key.split(",")
                if ((array_key[0] != val) && (array_key[1] != val)) {
                    temp_edges[key] = this.edges[key]
                }          
            }
            this.edges = temp_edges
        }
    }

    del_edge(val1, val2) {
        var item = String(val1) + "," + String(val2)
        if(item in this.edges) {
            delete this.edges[item]
        } else {
            throw 'That edge does not exist.'
        }
    }

    has_node(val) {
        return (val in this.node_list)
    }

    neighbors(val) {
        var output = []
        var temp_list = []
        for(var key in this.edges) {
            var array_key = key.split(",")
            if(array_key[0] == val) {
                temp_list.push(array_key[1])
            }
            if(array_key[1] == val) {
                    temp_list.push(array_key[0])
            }
        }
        for(var i = 0; i < temp_list.length; i++ ) {
            var the_num = parseInt(temp_list[i])
            if(!(output.includes(the_num))) {
                output.push(the_num)
            }
        } 
        return output
    }

    adjacent(val1, val2) {
        if(String(val1) + "," + String(val2) in this.edges) {
            return true
        }
        else {
            return false
        }
    } 
}

module.exports = {Graph}
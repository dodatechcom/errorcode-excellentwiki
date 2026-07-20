---
title: "[Solution] Python NetworkX Error — NodeNotFound, Graph Construction & Algorithm Failures"
description: "Fix Python NetworkX errors by resolving node issues, graph construction problems, and algorithm failures. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 407
---

# Python NetworkX Error — NodeNotFound, Graph Construction & Algorithm Failures

NetworkX errors occur when referencing nodes that don't exist, constructing graphs with incompatible data, or running algorithms on graphs with incorrect properties (e.g., directed vs undirected, weighted vs unweighted).

## Common Causes

```python
import networkx as nx

# 1. Adding edge with non-existent node reference
G = nx.Graph()
G.add_edge("A", "B")
G["C"]["D"]  # KeyError: node 'C' not in graph
```

```python
# 2. Running directed algorithm on undirected graph
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
nx.ancestors(G, "C")  # NetworkXError — only for DiGraph
```

```python
# 3. Weighted algorithm on unweighted graph
G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
nx.shortest_path_length(G, "A", "C", weight="weight")  # KeyError
```

```python
# 4. NodeAlreadyExists in strict graph
G = nx.DiGraph()
G.add_node("A", label="first")
G.add_node("A", label="second")  # overwrites silently, no error
```

```python
# 5. Empty graph in algorithm expecting edges
G = nx.Graph()
nx.shortest_path(G, "A", "B")  # NetworkXNoPath
```

## How to Fix

### Fix 1: Check node existence before accessing neighbors

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])

# Safe access
if "C" in G and "D" in G:
    print(G["C"]["D"])
else:
    print("One or both nodes not found")

# Use G.has_node() for single node checks
if G.has_node("A"):
    print(f"Neighbors of A: {list(G.neighbors('A'))}")
```

### Fix 2: Use correct graph type for algorithms

```python
import networkx as nx

# For ancestor/descendant operations, use DiGraph
DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("B", "C")])
ancestors = nx.ancestors(DG, "C")
print(f"Ancestors of C: {ancestors}")
```

### Fix 3: Set default weight attribute

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])

# Add default weight to all edges
for u, v in G.edges():
    G[u][v]["weight"] = 1

# Now weighted shortest path works
path = nx.shortest_path(G, "A", "C", weight="weight")
length = nx.shortest_path_length(G, "A", "C", weight="weight")
print(f"Path: {path}, Length: {length}")
```

### Fix 4: Handle empty or disconnected graphs

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([("A", "B")])

try:
    path = nx.shortest_path(G, "A", "C")
except nx.NetworkXNoPath:
    print("No path exists between these nodes")
except nx.NodeNotFound as e:
    print(f"Node not in graph: {e}")

# Check connectivity first
if nx.is_connected(G):
    print("Graph is connected")
else:
    components = list(nx.connected_components(G))
    print(f"Graph has {len(components)} components")
```

## Examples

```python
import networkx as nx

# Build and analyze a social network
G = nx.Graph()
edges = [
    ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"),
    ("Charlie", "David"), ("Eve", "Alice"), ("Eve", "Bob")
]
G.add_edges_from(edges)

# Compute centrality
centrality = nx.degree_centrality(G)
print("Degree centrality:", centrality)

# Find shortest path
path = nx.shortest_path(G, "Eve", "David")
print(f"Shortest path Eve->David: {path}")
```

## Related Errors

- [KeyError](/languages/python/keyerror/) — node not found in graph
- [ValueError](/languages/python/valueerror/) — invalid graph parameter
- [TypeError](/languages/python/typeerror/) — wrong graph type for operation

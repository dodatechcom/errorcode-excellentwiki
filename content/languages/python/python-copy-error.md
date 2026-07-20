---
title: "[Solution] Python Copy Error — Shallow and Deep Copy Issues"
description: "Fix Python copy errors by handling shallow vs deep copy, copy.copy/copy.deepcopy failures, and __copy__/__deepcopy__ methods. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 211
---

# Python Copy Error — Shallow and Deep Copy Issues

Copy errors occur when objects are not properly duplicated, when shallow copies don't replicate nested structures, or when custom `__copy__` and `__deepcopy__` methods are incorrectly implemented. Understanding the difference between shallow and deep copying is essential for avoiding unintended shared references.

## Common Causes

```python
# Shallow copy doesn't copy nested objects
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)

shallow[0][0] = 999
print(original)  # [[999, 2, 3], [4, 5, 6]] — original is modified!
```

```python
# Assignment is not a copy
original = [1, 2, 3]
not_a_copy = original

not_a_copy[0] = 999
print(original)  # [999, 2, 3] — both refer to the same list
```

```python
# deepcopy fails on objects with unpicklable attributes
import copy
import threading

class BadCopy:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = [1, 2, 3]

obj = BadCopy()
copy.deepcopy(obj)  # TypeError: cannot pickle '_thread.lock' object
```

```python
# Custom __copy__ method raises error
class CustomCopy:
    def __init__(self, value):
        self.value = value
    
    def __copy__(self):
        raise RuntimeError("Copy not allowed")

obj = CustomCopy(42)
copy.copy(obj)  # RuntimeError: Copy not allowed
```

```python
# Deep copy of objects with circular references
import copy

a = {"list": []}
b = {"parent": a}
a["list"].append(b)  # Circular reference

copy.deepcopy(a)  # Works but may be slow or use significant memory
```

## How to Fix

### Fix 1: Use deepcopy for nested structures

```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)

deep[0][0] = 999
print(original)  # [[1, 2, 3], [4, 5, 6]] — original unchanged
print(deep)      # [[999, 2, 3], [4, 5, 6]] — deep copy modified
```

### Fix 2: Implement __copy__ and __deepcopy__ for custom objects

```python
import copy

class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None  # Unpicklable resource
    
    def connect(self):
        self.connection = f"Connected to {self.host}:{self.port}"
    
    def __copy__(self):
        # Shallow copy: share the connection
        new_obj = DatabaseConnection(self.host, self.port)
        new_obj.connection = self.connection  # Shared reference
        return new_obj
    
    def __deepcopy__(self, memo):
        # Deep copy: create new connection
        new_obj = DatabaseConnection(
            copy.deepcopy(self.host, memo),
            copy.deepcopy(self.port, memo)
        )
        new_obj.connect()  # New independent connection
        return new_obj

# Usage
original = DatabaseConnection("localhost", 5432)
original.connect()

shallow = copy.copy(original)
deep = copy.deepcopy(original)

print(original.connection)  # Connected to localhost:5432
print(shallow.connection)   # Connected to localhost:5432 (shared)
print(deep.connection)      # Connected to localhost:5432 (independent)
```

### Fix 3: Use copy module functions correctly

```python
import copy

# copy.copy() — shallow copy
original = {"a": [1, 2], "b": [3, 4]}
shallow = copy.copy(original)
shallow["a"][0] = 999
print(original["a"])  # [999, 2] — nested list shared

# copy.deepcopy() — deep copy
deep = copy.deepcopy(original)
deep["b"][0] = 888
print(original["b"])  # [3, 4] — independent

# copy module also works with common types
import datetime
dt = datetime.datetime.now()
dt_copy = copy.copy(dt)
dt_deep = copy.deepcopy(dt)
```

### Fix 4: Handle unpicklable objects in deepcopy

```python
import copy
import threading

class SafeCopy:
    def __init__(self, data, lock=None):
        self.data = data
        self.lock = lock or threading.Lock()
    
    def __deepcopy__(self, memo):
        # Skip unpicklable attributes during deep copy
        new_obj = SafeCopy(
            copy.deepcopy(self.data, memo),
            threading.Lock()  # New lock for the copy
        )
        return new_obj
    
    def __copy__(self):
        # For shallow copy, share the lock
        new_obj = SafeCopy(self.data, self.lock)
        return new_obj

# Usage
original = SafeCopy([1, 2, 3])
deep = copy.deepcopy(original)
shallow = copy.copy(original)

deep.data[0] = 999
print(original.data)  # [1, 2, 3] — unchanged
print(deep.data)      # [999, 2, 3] — modified
```

### Fix 5: Use copy for common patterns

```python
import copy

# Pattern 1: Duplicate configuration
default_config = {
    "database": {"host": "localhost", "port": 5432},
    "debug": False,
    "log_level": "INFO"
}

user_config = copy.deepcopy(default_config)
user_config["database"]["host"] = "production.db.example.com"
user_config["debug"] = True

print(default_config["database"]["host"])  # localhost — unchanged
print(user_config["database"]["host"])     # production.db.example.com

# Pattern 2: Snapshot state before modification
class GameState:
    def __init__(self):
        self.score = 0
        self.inventory = []
        self.position = {"x": 0, "y": 0}
    
    def save_state(self):
        return copy.deepcopy(self)
    
    def restore_state(self, saved_state):
        self.score = saved_state.score
        self.inventory = saved_state.inventory
        self.position = saved_state.position

game = GameState()
game.score = 100
game.inventory.append("sword")
checkpoint = game.save_state()

game.score = 50
game.inventory.clear()
game.restore_state(checkpoint)
print(game.score)  # 100
```

## Examples

### Copy with custom collections

```python
import copy

class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    
    def add_child(self, child):
        self.children.append(child)
        return self
    
    def __deepcopy__(self, memo):
        new_tree = Tree(
            copy.deepcopy(self.value, memo),
            copy.deepcopy(self.children, memo)
        )
        return new_tree

# Build tree
root = Tree("root")
child1 = Tree("child1")
child2 = Tree("child2")
root.add_child(child1).add_child(child2)

# Deep copy the tree
tree_copy = copy.deepcopy(root)
tree_copy.value = "modified_root"
tree_copy.children[0].value = "modified_child1"

print(root.value)              # root
print(root.children[0].value)  # child1
print(tree_copy.value)         # modified_root
```

## Related Errors

- [TypeError](/languages/python/typeerror/) — copy functions receive incompatible objects
- [PicklingError](/languages/python/picklingerror/) — objects can't be serialized for deep copy
- [AttributeError](/languages/python/attributeerror/) — accessing non-existent copy methods

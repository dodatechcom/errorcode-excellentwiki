---
title: "[Solution] Python AST Error — Abstract Syntax Tree Parsing and Manipulation Issues"
description: "Fix Python AST errors by handling parse failures, AST node errors, code compilation, and ast.literal_eval issues. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 208
---

# Python AST Error — Abstract Syntax Tree Parsing and Manipulation Issues

AST errors occur when Python code cannot be parsed into a valid abstract syntax tree, when AST nodes are incorrectly accessed or modified, or when ast.literal_eval encounters invalid literals. The ast module provides tools for parsing, analyzing, and transforming Python code.

## Common Causes

```python
# Parsing invalid Python syntax
import ast

code = "def foo(: pass"  # Missing closing parenthesis
tree = ast.parse(code)  # SyntaxError: invalid syntax
```

```python
# ast.literal_eval with non-literal expressions
import ast

ast.literal_eval("2 + 3")  # ValueError: only strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None are supported
ast.literal_eval("os.system('ls')")  # ValueError: malformed node or string
```

```python# Accessing non-existent AST node attributes
import ast

code = "x = 42"
tree = ast.parse(code)
assign = tree.body[0]

assign.nonexistent_attribute  # AttributeError: 'Assign' object has no attribute 'nonexistent_attribute'
```

```python
# Compiling AST with wrong mode
import ast

code = "x = 42"
tree = ast.parse(code)
compile(tree, "<string>", "exec")  # Works
compile(tree, "<string>", "eval")  # TypeError: cannot compile an expression AST in eval mode
```

```python
# Modifying AST incorrectly — wrong node types
import ast

code = "x = 1"
tree = ast.parse(code)
assign = tree.body[0]

# Trying to modify a constant node directly
assign.value = ast.Constant(value="new_value")  # May cause unexpected behavior
```

## How to Fix

### Fix 1: Handle parse errors gracefully

```python
import ast

def safe_parse(source_code):
    """Safely parse Python source code into an AST."""
    try:
        tree = ast.parse(source_code)
        return tree, None
    except SyntaxError as e:
        return None, f"Syntax error at line {e.lineno}: {e.msg}"
    except TypeError as e:
        return None, f"Type error: {e}"

# Usage
code = "def foo(): pass"
tree, error = safe_parse(code)
if error:
    print(f"Parse failed: {error}")
else:
    print(f"Parsed successfully: {ast.dump(tree)}")
```

### Fix 2: Use ast.literal_eval for safe evaluation

```python
import ast

def safe_eval(value_string):
    """Safely evaluate a string as a Python literal."""
    try:
        return ast.literal_eval(value_string), None
    except (ValueError, SyntaxError) as e:
        return None, f"Invalid literal: {e}"

# Usage
value, error = safe_eval("{'key': [1, 2, 3]}")
print(value)  # {'key': [1, 2, 3]}

value, error = safe_eval("2 + 3")
print(error)  # Invalid literal: only strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and None are supported
```

### Fix 3: Inspect and modify AST nodes correctly

```python
import ast

def analyze_code(source_code):
    """Analyze Python code using AST."""
    tree = ast.parse(source_code)
    
    info = {
        "functions": [],
        "variables": [],
        "imports": [],
        "classes": [],
    }
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            info["functions"].append({
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "line": node.lineno,
            })
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    info["variables"].append(target.id)
        elif isinstance(node, ast.ClassDef):
            info["classes"].append({
                "name": node.name,
                "line": node.lineno,
            })
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            info["imports"].append(ast.dump(node))
    
    return info

code = """
import os

class Calculator:
    def __init__(self, value):
        self.value = value
    
    def add(self, x):
        return self.value + x

x = 42
"""
print(analyze_code(code))
```

### Fix 4: Transform AST safely

```python
import ast

class RenameVariables(ast.NodeTransformer):
    """Rename variables in an AST."""
    
    def __init__(self, renames):
        self.renames = renames
    
    def visit_Name(self, node):
        if node.id in self.renames:
            node.id = self.renames[node.id]
        return self.generic_visit(node)

code = "x = 1\ny = x + 2"
tree = ast.parse(code)
transformer = RenameVariables({"x": "a", "y": "b"})
new_tree = transformer.visit(tree)
ast.fix_missing_locations(new_tree)

# Compile and execute
code_obj = compile(new_tree, "<string>", "exec")
exec(code_obj)  # Now uses 'a' and 'b' instead of 'x' and 'y'
```

### Fix 5: Compile AST with correct mode

```python
import ast

def compile_code(source_code, mode="exec"):
    """Compile source code with the correct mode."""
    tree = ast.parse(source_code)
    
    if mode == "exec":
        # For statements and modules
        return compile(tree, "<string>", "exec")
    elif mode == "eval":
        # For single expressions
        if len(tree.body) == 1 and isinstance(tree.body[0], ast.Expr):
            return compile(tree.body[0].value, "<string>", "eval")
        else:
            raise ValueError("eval mode requires a single expression")
    elif mode == "single":
        # For interactive mode
        return compile(tree, "<string>", "single")
    else:
        raise ValueError(f"Invalid mode: {mode}")

# Usage
code = "result = 2 + 3"
code_obj = compile_code(code, "exec")
exec(code_obj)
print(result)  # 5

expr = "2 + 3"
code_obj = compile_code(expr, "eval")
print(eval(code_obj))  # 5
```

## Examples

### AST-based code linter

```python
import ast

class SimpleLinter(ast.NodeVisitor):
    """Simple linter that checks for common issues."""
    
    def __init__(self):
        self.issues = []
    
    def visit_FunctionDef(self, node):
        # Check for missing docstrings
        if not ast.get_docstring(node):
            self.issues.append(f"Line {node.lineno}: Function '{node.name}' missing docstring")
        
        # Check for too many arguments
        if len(node.args.args) > 5:
            self.issues.append(f"Line {node.lineno}: Function '{node.name}' has too many arguments")
        
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        if not ast.get_docstring(node):
            self.issues.append(f"Line {node.lineno}: Class '{node.name}' missing docstring")
        self.generic_visit(node)

code = """
class Calculator:
    def add(self, a, b, c, d, e, f):
        return a + b + c + d + e + f
"""

tree = ast.parse(code)
linter = SimpleLinter()
linter.visit(tree)
for issue in linter.issues:
    print(issue)
```

### AST dump for debugging

```python
import ast

code = """
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = greet("World")
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=2))
```

## Related Errors

- [SyntaxError](/languages/python/syntaxerror/) — AST parse failures due to invalid syntax
- [ValueError](/languages/python/valueerror/) — ast.literal_eval rejects non-literal expressions
- [TypeError](/languages/python/typeerror/) — incorrect AST node types or modes

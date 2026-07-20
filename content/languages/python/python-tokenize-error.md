---
title: "[Solution] Python Tokenize Error — Tokenization Failures and Encoding Issues"
description: "Fix Python tokenize errors by handling TokenError, tokenization failures, encoding detection, and comment handling. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 207
---

# Python Tokenize Error — Tokenization Failures and Encoding Issues

Tokenize errors occur when Python's tokenizer encounters invalid syntax, encoding declarations, unterminated strings, or encoding mismatches. These errors are often the first sign of syntax problems in source code.

## Common Causes

```python
# Unterminated string literal
import tokenize
import io

code = 'x = "hello world'
tokens = tokenize.generate_tokens(io.StringIO(code).readline)
for tok in tokens:
    pass  # TokenError: EOL while scanning string literal
```

```python
# Invalid encoding declaration
import tokenize

code = b"# -*- coding: invalid-encoding -*-\nprint('hello')"
tokens = list(tokenize.tokenize(io.BytesIO(code).readline))
# TokenError: unknown encoding: invalid-encoding
```

```python
# Encoding mismatch between declaration and content
import tokenize
import io

# File declares UTF-8 but contains invalid UTF-8 bytes
code = b"# -*- coding: utf-8 -*-\nprint('\xff\xfe')"
tokens = list(tokenize.tokenize(io.BytesIO(code).readline))
# TokenError or UnicodeDecodeError
```

```python
# Indentation errors detected during tokenization
import tokenize
import io

code = """def foo():
    x = 1
  y = 2  # IndentationError detected during tokenization
"""
tokens = tokenize.generate_tokens(io.StringIO(code).readline)
for tok in tokens:
    pass  # IndentationError: unindent does not match outer indentation
```

```python
# Invalid token in source code
import tokenize
import io

code = "x = 1 @ 2"  # @ is not valid in this context
tokens = tokenize.generate_tokens(io.StringIO(code).readline)
for tok in tokens:
    pass  # SyntaxError: invalid syntax
```

## How to Fix

### Fix 1: Use tokenize to validate source code

```python
import tokenize
import io
import token

def validate_python_code(source_code):
    """Validate Python source code by tokenizing it."""
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(source_code).readline))
        return True, None
    except tokenize.TokenError as e:
        return False, f"Token error: {e}"
    except IndentationError as e:
        return False, f"Indentation error: {e}"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"

# Usage
code = """
def add(a, b):
    return a + b
"""
is_valid, error = validate_python_code(code)
if is_valid:
    print("Code is valid")
else:
    print(f"Invalid code: {error}")
```

### Fix 2: Handle encoding declarations properly

```python
import tokenize
import io

# Method 1: Let tokenize auto-detect encoding (default behavior)
with open("script.py", "rb") as f:
    encoding = tokenize.detect_encoding(f.readline)[0]
    print(f"Detected encoding: {encoding}")

# Method 2: Specify encoding explicitly
code = "# -*- coding: utf-8 -*-\nprint('Hello, world!')"
tokens = list(tokenize.tokenize(io.BytesIO(code.encode("utf-8")).readline))
for tok in tokens:
    if tok.type == token.NAME:
        print(f"Name: {tok.string}")
```

### Fix 3: Parse tokens to extract meaningful information

```python
import tokenize
import io
import token

def extract_function_names(source_code):
    """Extract function names from Python source code."""
    functions = []
    tokens = list(tokenize.generate_tokens(io.StringIO(source_code).readline))
    
    for i, tok in enumerate(tokens):
        if tok.type == token.NAME and tok.string == "def":
            # Next token should be the function name
            if i + 1 < len(tokens):
                func_name = tokens[i + 1].string
                functions.append(func_name)
    
    return functions

code = """
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""
print(extract_function_names(code))  # ['add', 'subtract']
```

### Fix 4: Use ast instead of tokenize for higher-level analysis

```python
import ast

def analyze_code_structure(source_code):
    """Analyze code structure using AST (preferred over tokenize)."""
    tree = ast.parse(source_code)
    
    info = {
        "functions": [],
        "classes": [],
        "imports": [],
    }
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            info["functions"].append(node.name)
        elif isinstance(node, ast.ClassDef):
            info["classes"].append(node.name)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            info["imports"].append(ast.dump(node))
    
    return info

code = """
import os
from pathlib import Path

class MyClass:
    def method(self):
        pass

def standalone():
    pass
"""
print(analyze_code_structure(code))
```

### Fix 5: Handle multi-line strings and comments

```python
import tokenize
import io
import token

def extract_comments_and_strings(source_code):
    """Extract comments and string literals from source code."""
    comments = []
    strings = []
    
    for tok in tokenize.generate_tokens(io.StringIO(source_code).readline):
        if tok.type == token.COMMENT:
            comments.append(tok.string)
        elif tok.type == token.STRING:
            strings.append(tok.string)
    
    return comments, strings

code = '''
# This is a comment
x = "hello world"
y = 'another string'
# Another comment
z = """Multi-line
string"""
'''
comments, strings = extract_comments_and_strings(code)
print("Comments:", comments)
print("Strings:", strings)
```

## Examples

### Tokenizing a file with error handling

```python
import tokenize
import io
import sys

def tokenize_file(filepath):
    """Safely tokenize a Python file."""
    try:
        with open(filepath, "rb") as f:
            tokens = list(tokenize.tokenize(f.readline))
            for tok in tokens:
                print(f"{token.tok_name[tok.type]:10} {tok.string!r:30} line {tok.start[0]}")
    except tokenize.TokenError as e:
        print(f"Tokenization error: {e}", file=sys.stderr)
        return False
    except IndentationError as e:
        print(f"Indentation error: {e}", file=sys.stderr)
        return False
    except SyntaxError as e:
        print(f"Syntax error: {e}", file=sys.stderr)
        return False
    return True

# tokenize_file("script.py")
```

### Custom tokenizer with preprocessing

```python
import tokenize
import io
import re

def preprocess_and_tokenize(source_code):
    """Preprocess source code before tokenizing."""
    # Remove trailing whitespace from each line
    lines = source_code.split("\n")
    cleaned = "\n".join(line.rstrip() for line in lines)
    
    # Remove blank lines at the end
    cleaned = cleaned.rstrip() + "\n"
    
    tokens = list(tokenize.generate_tokens(io.StringIO(cleaned).readline))
    return tokens

code = "x = 1   \ny = 2\n"
tokens = preprocess_and_tokenize(code)
for tok in tokens:
    if tok.type not in (tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT):
        print(tok)
```

## Related Errors

- [SyntaxError](/languages/python/syntaxerror/) — tokenize often detects syntax errors first
- [IndentationError](/languages/python/indentationerror/) — indentation issues found during tokenization
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding problems in source files

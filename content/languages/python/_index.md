---
title: "[Solution] Python Errors & Exceptions — Complete Reference"
description: "Find solutions for Python errors and exceptions. Fix TypeError, ValueError, KeyError, and more with copy-paste code examples."
languages: ["python"]
---

Python exceptions are raised at runtime when something goes wrong — from passing the wrong argument type to failing to import a module. Every entry below includes a clear explanation of what triggers the error and the exact code fix.

## Error Codes

| Error | Description | Fix |
|-------|-------------|-----|
| [AttributeError](/languages/python/attributeerror/) | Object has no attribute — accessing a non-existent attribute or method | Check the object type with `type()`, verify the attribute name, and handle `None` returns |
| [FileNotFoundError](/languages/python/filenotfounderror/) | No such file or directory — the file path does not exist | Use `os.path.exists()` to check before opening, and verify the path string |
| [ImportError](/languages/python/importerror/) | Module not found or cannot import name — missing package or circular import | Install the package with `pip install`, check the module name, and resolve circular dependencies |
| [IndentationError](/languages/python/indentationerror/) | Unexpected indent or unindent — inconsistent whitespace | Use spaces consistently (PEP 8 recommends 4), and enable editor whitespace display |
| [IndexError](/languages/python/indexerror/) | List index out of range — accessing beyond the list length | Check the list length with `len()`, use `enumerate()`, and handle empty lists |
| [KeyError](/languages/python/keyerror/) | Dictionary key not found — accessing a missing dictionary key | Use `dict.get(key, default)`, check `key in dict` first, or use `dict.setdefault()` |
| [SyntaxError](/languages/python/syntaxerror/) | Invalid syntax — code cannot be parsed before execution | Review the line number, check for missing colons, brackets, or quotes |
| [TypeError](/languages/python/typeerror/) | Unsupported operand type — operation applied to wrong type | Convert types explicitly, check `isinstance()`, and validate function arguments |
| [ValueError](/languages/python/valueerror/) | Invalid argument — correct type but wrong value | Validate input before conversion, use try/except, and check boundary conditions |
| [ZeroDivisionError](/languages/python/zerodivisionerror/) | Division by zero — mathematical operation with zero divisor | Add input validation, check for zero before dividing, and use `math.isclose()` for floats |

## Quick Debug

```python
# Show the full traceback in a script
import traceback
try:
    risky_operation()
except Exception as e:
    traceback.print_exc()
```

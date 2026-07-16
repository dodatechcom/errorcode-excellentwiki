---
title: "[Solution] Python reload() Deprecated — Use importlib.reload()"
description: "Replace deprecated builtin reload() with importlib.reload() in Python 3. Migration guide for module reloading with proper usage patterns."
deprecated_function: "reload"
replacement_function: "importlib.reload"
languages: ["python"]
deprecated_since: "Python 3.0"
removed_in: "Python 3.0"
error_message: "NameError: name 'reload' is not defined"
tags: ["reload", "importlib", "python2", "python3", "module-reload"]
weight: 38
---

# [Solution] Python reload() Deprecated — Use importlib.reload()

The `reload()` built-in function was moved from the global namespace to `importlib.reload()` in Python 3. It reloads a previously imported module, re-executing its top-level code. This is useful during development when you have modified a module and want to see the changes without restarting the interpreter. In Python 2, `reload()` was a built-in; in Python 3, you must `import importlib` first.

## What You'll See

In Python 3, if you call `reload()` without importing it:

```python
import mymodule
reload(mymodule)  # NameError: name 'reload' is not defined
```

## Why Changed

`reload()` was moved to `importlib` because:

- **Namespace pollution**: Having `reload()` as a built-in clutters the global namespace.
- **Clarity**: Explicit import makes the intent clear and avoids confusion.
- **Consistency**: Module operations belong in the `importlib` module alongside `import_module()`.
- **Safety**: The move forces developers to think about when and why they are reloading modules.

## Old Code (Python 2)

```python
import mymodule

# Modify the module (e.g., in a file)
# Then reload without restarting the interpreter
reload(mymodule)

# Reload multiple modules
reload(module_a)
reload(module_b)

# In interactive Python 2, reload was available directly
>>> import math
>>> reload(math)
```

## New Code (Python 3)

```python
import importlib
import mymodule

# Reload the module
importlib.reload(mymodule)

# Reload multiple modules
importlib.reload(module_a)
importlib.reload(module_b)

# You can also use the module object directly
import mymodule
importlib.reload(mymodule)
```

## Practical Usage: Development Reload Helper

```python
import importlib
import sys

def reload_module(module_name):
    """Reload a module by name. Returns the reloaded module or None."""
    if module_name not in sys.modules:
        print(f"Module '{module_name}' is not imported")
        return None

    module = sys.modules[module_name]
    try:
        importlib.reload(module)
        print(f"Reloaded '{module_name}'")
        return module
    except Exception as e:
        print(f"Failed to reload '{module_name}': {e}")
        return None

# Usage
reload_module("myapp.utils")
reload_module("myapp.config")
```

## Practical Usage: Flask/Auto-Reload Pattern

```python
# Common in Flask development — reload on code change
from flask import Flask
import importlib
import os

app = Flask(__name__)

@app.route("/reload/<module_name>")
def reload_route(module_name):
    """Endpoint to reload modules during development."""
    import sys
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
        return f"Reloaded {module_name}"
    return f"Module {module_name} not found"
```

## Migration Steps

1. **Find all reload calls**:

```bash
grep -rn "\breload\s*(" --include="*.py" /path/to/project/
```

2. **Add the import** at the top of each file that uses reload:

```python
import importlib
```

3. **Replace `reload(module)` with `importlib.reload(module)`**.

4. **Verify the module is already imported** before reloading:

```python
import sys
if "mymodule" in sys.modules:
    importlib.reload(sys.modules["mymodule"])
```

5. **Consider whether you really need reload.** In production code, module reloading can cause subtle issues:
   - Existing references to old module objects are not updated.
   - Module-level state may be inconsistent after reload.
   - Circular imports may behave differently.

6. **Search for related patterns**:

```bash
grep -rn "execfile\|reload\b" --include="*.py" /path/to/project/
```

## When to Use Module Reloading

| Scenario | Recommended |
|---|---|
| Interactive Python shell during development | Yes — use `importlib.reload()` |
| Flask/Django development server | Usually handled by the framework's auto-reloader |
| Production code | No — restart the application instead |
| Unit tests | No — import modules fresh in each test |
| Plugin systems | Consider alternatives (e.g., importlib for fresh imports) |

## Safer Alternative: Fresh Import

```python
# Instead of reloading, remove and re-import
import sys
import importlib

def fresh_import(module_name):
    """Remove a module from cache and re-import it."""
    if module_name in sys.modules:
        del sys.modules[module_name]
    return importlib.import_module(module_name)

# Usage
mymodule = fresh_import("myapp.utils")
```

## Related Errors

- [execfile() → exec(open().read())](execfile-to-exec) — Python file execution migration.
- [print statement → print()](print-statement) — Python print syntax change.

---
title: "[Solution] Python execfile() Deprecated — Use exec(open().read())"
description: "Replace deprecated execfile() with exec(open().read()) or importlib in Python 3. Migration guide with before/after code and best practices."
deprecated_function: "execfile"
replacement_function: "exec(open().read())"
languages: ["python"]
deprecated_since: "Python 3.0"
removed_in: "Python 3.0"
error_message: "NameError: name 'execfile' is not defined"
tags: ["execfile", "exec", "python2", "python3", "migration"]
weight: 35
---

# [Solution] Python execfile() Deprecated — Use exec(open().read())

The `execfile()` built-in function was removed in Python 3. It read a file and executed its contents as Python code, similar to a `#include` in C. The replacement is `exec(open(filename).read())`, though for most use cases you should prefer importing the file as a module instead. Executing file contents as code is generally discouraged — it bypasses static analysis, makes debugging harder, and can introduce security risks.

## What You'll See

In Python 3, if your code calls `execfile()`:

```python
execfile("config.py")
```

You get:

```
NameError: name 'execfile' is not defined
```

## Why Removed

`execfile()` was removed in Python 3 because:

- **Ambiguity with exec()**: The language already had `exec()`, and `execfile()` was trivially replaceable.
- **Security concerns**: Reading and executing arbitrary files is a security risk.
- **Poor debugging**: Code executed via `execfile()` does not appear in tracebacks with proper file names.
- **No static analysis**: Tools like linters and type checkers cannot analyze code executed this way.

## Old Code (Python 2)

```python
# Execute a configuration file
execfile("config.py")

# Execute with a custom global namespace
execfile("setup.py", {"verbose": True})

# Execute with both global and local namespaces
execfile("template.py", globals(), locals())

# Common pattern: loading environment variables
execfile(".env.py")
print(DATABASE_URL)  # variable defined in .env.py
```

## New Code — Direct Replacement

```python
# Simple replacement for execfile()
def execfile(filename, globals_dict=None, locals_dict=None):
    if globals_dict is None:
        globals_dict = {}
    with open(filename) as f:
        exec(compile(f.read(), filename, "exec"), globals_dict, locals_dict)

# Usage
execfile("config.py")

# With custom namespace
execfile("setup.py", {"verbose": True})
```

## New Code — Using exec() Directly

```python
# Direct replacement without helper function
exec(open("config.py").read())

# With explicit namespace
namespace = {"verbose": True}
exec(open("setup.py").read(), namespace)

# With safe file handling
with open("config.py") as f:
    exec(f.read())
```

## New Code — Import as Module (Recommended)

```python
# BEST: Import the file as a module instead of executing it
import importlib.util

def load_module_from_file(filepath, module_name):
    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Usage
config = load_module_from_file("config.py", "config")
print(config.DATABASE_URL)
```

## New Code — Simple Configuration Pattern

```python
# Old: config.py executed with execfile
# DATABASE_URL = "postgres://localhost/mydb"
# SECRET_KEY = "abc123"

# New: config.py imported as a module
# Same file content, but imported instead of executed
import config
print(config.DATABASE_URL)

# Or use a proper configuration library
# pip install python-dotenv
from dotenv import load_dotenv
import os

load_dotenv(".env")
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
```

## Migration Steps

1. **Find all execfile calls**:

```bash
grep -rn "execfile" --include="*.py" /path/to/project/
```

2. **Determine what the executed file does.** If it defines variables (config), convert it to a module import. If it performs actions, consider wrapping those actions in a function.

3. **Replace `execfile("file.py")` with `exec(open("file.py").read())`** as a quick fix.

4. **Better: Convert the executed file to a proper module** and import it.

5. **Best: Use a configuration library** (like `python-dotenv` for env files, or `configparser` for INI files) instead of executing Python code for configuration.

6. **Test that all variables and side effects** from the executed file are still available in the expected scope.

## Migration Using 2to3

The `2to3` tool handles this conversion:

```bash
# Preview changes
2to3 -f execfile -d script.py

# Apply changes
2to3 -f execfile -w script.py
```

## Related Errors

- [reload() → importlib.reload()](reload-to-importlib) — Python module reload migration.
- [print statement → print()](print-statement) — Python print syntax change.

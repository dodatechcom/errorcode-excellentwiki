---
title: "[Solution] Python 3.9 Deprecation — threading, importlib.abc, json Changes"
description: "Fix Python 3.9 deprecation warnings from threading deprecations, importlib.abc removal, json.load() changes, and locale modifications."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 505
---

# Python 3.9 Deprecation — threading, importlib.abc, json Changes

Python 3.9 deprecates several threading APIs, removes `importlib.abc` module-level classes, changes JSON parsing behavior, and modifies locale handling. These deprecations became removals in Python 3.12.

## Common Causes

```python
# Cause 1: threading method name deprecations
import threading
t = threading.Thread()
t.isAlive()  # Deprecated — use is_alive()

# Cause 2: importlib.abc classes removed from module level
from importlib.abc import Loader, Finder  # Deprecated path

# Cause 3: json.load() with bytes/bytearray argument
import json
data = json.loads(b'{"key": "value"}')  # Deprecated behavior

# Cause 4: locale.getdefaultlocale() deprecation
import locale
locale.getdefaultlocale()  # Deprecated in 3.11

# Cause 5: hashlib.md5() used for security
import hashlib
h = hashlib.md5(usedforsecurity=False)  # Parameter added
```

## How to Fix

### Fix 1: Update threading method calls

```python
# Wrong — deprecated threading methods
import threading

t = threading.Thread(target=worker)
t.isAlive()        # Deprecated
t.getName()        # Deprecated
t.setName("name")  # Deprecated
t.isDaemon()       # Deprecated
t.setDaemon(True)  # Deprecated
count = threading.activeCount()  # Deprecated
current = threading.currentThread()  # Deprecated

# Correct — use lowercase versions
t = threading.Thread(target=worker)
t.is_alive()
t.name
t.name = "name"
t.daemon = True
count = threading.active_count()
current = threading.current_thread()
```

### Fix 2: Update importlib.abc imports

```python
# Wrong — deprecated importlib.abc path
from importlib.abc import Loader, Finder, MetaPathFinder
from importlib import abc

# Correct — use importlib.abc but check version
import sys
if sys.version_info >= (3, 12):
    # In 3.12+, use importlib.abc directly
    from importlib.abc import Loader
else:
    from importlib.abc import Loader  # Still works in 3.9-3.11

# For custom loaders, inherit from the right class
from importlib.abc import Loader

class MyLoader(Loader):
    def create_module(self, spec):
        return None

    def exec_module(self, module):
        pass
```

### Fix 3: Fix json.loads() with bytes input

```python
# Wrong — passing bytes to json.loads (deprecated)
import json
data = b'{"key": "value"}'
result = json.loads(data)

# Correct — decode bytes first
import json
data = b'{"key": "value"}'
result = json.loads(data.decode("utf-8"))

# Or use json.load() with a file-like object
import json
import io
data = io.BytesIO(b'{"key": "value"}')
result = json.load(data)
```

### Fix 4: Use locale.getencoding() instead of getdefaultlocale

```python
# Wrong — locale.getdefaultlocale deprecated
import locale
lang, encoding = locale.getdefaultlocale()

# Correct — use locale.getencoding() (3.11+) or sys.getdefaultencoding()
import sys
encoding = sys.getdefaultencoding()

# Cross-version safe approach
import sys
if sys.version_info >= (3, 11):
    import locale
    encoding = locale.getencoding()
else:
    encoding = sys.getdefaultencoding()
```

## Examples

```python
# Thread lifecycle management migration
# Old:
# import threading
# def check_threads():
#     for t in threading.enumerate():
#         if t.isAlive() and t.isDaemon():
#             print(f"Daemon thread {t.getName()} is running")

# New:
import threading

def check_threads():
    for t in threading.enumerate():
        if t.is_alive() and t.daemon:
            print(f"Daemon thread {t.name} is running")

# Custom loader migration
# Old:
# from importlib.abc import Loader as OldLoader
# from importlib.machinery import ModuleSpec

# New:
from importlib.abc import Loader
from importlib.machinery import ModuleSpec

class CustomLoader(Loader):
    def __init__(self, path):
        self.path = path

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        with open(self.path) as f:
            exec(f.read(), module.__dict__)

# JSON handling
# Old:
# import json
# raw = open("data.json", "rb").read()
# data = json.loads(raw)  # Deprecated bytes input

# New:
import json
with open("data.json", "r") as f:
    data = json.load(f)

# Or for bytes:
raw = b'{"key": "value"}'
data = json.loads(raw.decode("utf-8"))
```

## Related Errors

- [python310-deprecation](../python310-deprecation) — Python 3.10 threading deprecations
- [python311-deprecation](../python311-deprecation) — Python 3.11 removals
- [python312-deprecation](../python312-deprecation) — Python 3.12 importlib.abc removal
- [python-threading-error](../python-threading-error) — Threading issues
- [jsondecodeerror](../jsondecodeerror) — JSON parsing errors

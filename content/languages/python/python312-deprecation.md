---
title: "[Solution] Python 3.12 Deprecation — distutils Removal, Imp Module, Argparse Changes"
description: "Fix Python 3.12 deprecation errors from distutils removal, imp module deletion, sqlite3 adapter changes, and more. Migration examples included."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 501
---

# Python 3.12 Deprecation — distutils Removal, Imp Module, Argparse Changes

Python 3.12 removed several long-deprecated modules and changed default behaviors. Code relying on `distutils`, `imp`, or older sqlite3 adapters will break immediately on upgrade.

## Common Causes

```python
# Cause 1: distutils completely removed
from distutils.core import setup
setup(name="my-package", version="1.0")

# Cause 2: imp module fully removed (was deprecated since 3.4)
import imp
loader = imp.find_module("json")

# Cause 3: sqlite3 default adapter for datetime removed
import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE t (d TIMESTAMP)")
conn.execute("INSERT INTO t VALUES (?)", (datetime.now(),))  # No implicit adapter

# Cause 4: unittest deprecated aliases removed
import unittest
result = unittest.TestResult()
result.addSuccess(None)  # Removed — use addSuccess alias

# Cause 5: argparse type= callable deprecation
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--count", type=int)  # Still works, but type= behavior changed
```

## How to Fix

### Fix 1: Replace distutils with setuptools

```python
# Wrong — distutils removed in 3.12
from distutils.core import setup

# Correct — use setuptools
from setuptools import setup
setup(name="my-package", version="1.0")

# Or use pyproject.toml (recommended)
# [build-system]
# requires = ["setuptools>=64"]
# build-backend = "setuptools.backends._legacy:_Backend"
```

### Fix 2: Replace imp with importlib

```python
# Wrong — imp module removed
import imp
loader = imp.find_module("json")
mod = imp.load_module("json", *loader)

# Correct — use importlib
import importlib
loader = importlib.util.find_spec("json")
mod = importlib.util.module_from_spec(loader)
loader.loader.exec_module(mod)

# Or simply
import json
```

### Fix 3: Register custom sqlite3 adapters

```python
import sqlite3
import datetime

# Wrong — relying on implicit datetime adapter (removed in 3.12)
conn = sqlite3.connect(":memory:")
conn.execute("INSERT INTO t VALUES (?)", (datetime.datetime.now(),))

# Correct — register explicit adapters
def adapt_datetime(dt):
    return dt.isoformat()

def convert_datetime(s):
    return datetime.datetime.fromisoformat(s.decode())

sqlite3.register_adapter(datetime.datetime, adapt_datetime)
sqlite3.register_converter("TIMESTAMP", convert_datetime)

conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
conn.execute("CREATE TABLE t (d TIMESTAMP)")
conn.execute("INSERT INTO t VALUES (?)", (datetime.datetime.now(),))
```

### Fix 4: Update unittest method names

```python
# Wrong — deprecated unittest aliases removed in 3.12
import unittest

class Test(unittest.TestCase):
    def test_something(self):
        pass

# Use standard method names (no aliases needed)
# assertTrue, assertFalse, assertEqual, etc. — these are the canonical names
```

## Examples

```python
# Migrating a setup.py project to 3.12
# Before:
# from distutils.core import setup
# setup(name="myapp", version="0.1", py_modules=["mymod"])

# After:
from setuptools import setup, find_packages
setup(
    name="myapp",
    version="0.2",
    packages=find_packages(),
)

# Before (imp usage):
import imp
def load_module(name):
    file, path, desc = imp.find_module(name)
    return imp.load_module(name, file, path, desc)

# After:
import importlib
def load_module(name):
    spec = importlib.util.find_spec(name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod
```

## Related Errors

- [ImportError](../importerror) — Module-level import failures
- [DeprecationWarning](../deprecationwarning) — General deprecation warnings
- [python313-deprecation](../python313-deprecation) — Python 3.13 deprecation changes
- [python311-deprecation](../python311-deprecation) — Python 3.11 deprecation changes

---
title: "[Solution] Python AttributeError — Module Has No Attribute"
description: "Fix Python AttributeError when accessing non-existent module attributes. Learn why module attribute errors occur and how to fix them."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["attributeerror", "module", "attribute", "import"]
weight: 5
---

# AttributeError — Module Has No Attribute

An `AttributeError` with the message "module 'X' has no attribute 'Y'" is raised when you try to access an attribute that doesn't exist on a module. This is commonly caused by typos, wrong imports, or using an attribute from the wrong version of a library.

## Description

Modules have a fixed set of attributes defined in their source code. Attempting to access an attribute that doesn't exist raises `AttributeError`. This is different from `ModuleNotFoundError`, which means the module itself cannot be found.

Common patterns:

- **Typo in attribute name** — `math.sqtr(4)` instead of `math.sqrt(4)`.
- **Wrong module** — accessing an attribute from the wrong module.
- **Missing import** — using a name that was never imported.
- **Version mismatch** — attribute doesn't exist in the installed version.
- **Private attributes** — accessing `__private` attributes incorrectly.

## Common Causes

```python
# Cause 1: Typo in attribute name
import math
result = math.sqtr(4)  # AttributeError: module 'math' has no attribute 'sqtr'

# Cause 2: Wrong module
import os
result = os.sqrt(4)  # AttributeError: module 'os' has no attribute 'sqrt'

# Cause 3: Missing import
import json
data = json.XML_Parser()  # AttributeError — XML_Parser doesn't exist in json

# Cause 4: Version mismatch
import pandas as pd
df = pd.DataFrame()
df.to_jsonl()  # AttributeError — method may not exist in your version
```

## Solutions

### Fix 1: Check available attributes with dir()

```python
import math

# Debug — see what's available
print(dir(math))

# Or search for specific patterns
print([attr for attr in dir(math) if 'sqrt' in attr])
```

### Fix 2: Verify the correct module

```python
# Wrong
import os
os.sqrt(4)  # AttributeError

# Correct
import math
math.sqrt(4)  # Returns 2.0
```

### Fix 3: Use hasattr() to check before accessing

```python
import json

# Wrong
data = json.XML_Parser()

# Correct
if hasattr(json, 'XML_Parser'):
    data = json.XML_Parser()
else:
    print("XML_Parser is not available in json module")
```

### Fix 4: Check library documentation for correct method names

```python
import pandas as pd

# Check what methods are available
df = pd.DataFrame({'a': [1, 2, 3]})
print([m for m in dir(df) if not m.startswith('_')])
```

## Related Errors

- [Module not callable](module-not-callable) — calling a module instead of a function.
- [ImportError](../importerror) — module cannot be imported.
- [AttributeError](../attributeerror) — general attribute errors on objects.

---
title: "[Solution] Deprecated Function Migration: DataFrame.applymap to DataFrame.map"
description: "Migrate from deprecated pandas DataFrame.applymap() to DataFrame.map() for element-wise operations."
deprecated_function: "df.applymap()"
replacement_function: "df.map()"
languages: ["python"]
deprecated_since: "pandas 2.1+"
---

# [Solution] Deprecated Function Migration: DataFrame.applymap to DataFrame.map

The `df.applymap()` has been deprecated in favor of `df.map()`.

## Migration Guide

DataFrame.applymap() was deprecated in pandas 2.1.0 in favor of DataFrame.map().

## Before (Deprecated)

```python
import pandas as pd

df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
result = df.applymap(lambda x: x * 2)
```

## After (Modern)

```python
import pandas as pd

df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
result = df.map(lambda x: x * 2)
```

## Key Differences

- Simply rename applymap to map
- Same signature and behavior
- Available in pandas 2.1+

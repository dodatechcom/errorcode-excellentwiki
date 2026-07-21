---
title: "[Solution] Deprecated Function Migration: pickle.load to safer alternatives"
description: "Migrate from deprecated pickle.load with untrusted data to safer formats."
deprecated_function: "pickle.load(f)"
replacement_function: "json.load(f)"
languages: ["python"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: pickle.load to safer alternatives

The `pickle.load(f)` has been deprecated in favor of `json.load(f)`.

## Migration Guide

pickle.load can execute arbitrary code.

## Before (Deprecated)

```python
import pickle
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
```

## After (Modern)

```python
import json
with open("data.json") as f:
    data = json.load(f)
```

## Key Differences

- Never pickle.load untrusted data

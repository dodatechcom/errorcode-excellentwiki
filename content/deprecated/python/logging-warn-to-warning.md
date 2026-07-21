---
title: "[Solution] Deprecated Function Migration: logging.warn() to logging.warning()"
description: "Migrate from deprecated logging.warn() to logging.warning() in Python for PEP compliant logging."
deprecated_function: "logging.warn()"
replacement_function: "logging.warning()"
languages: ["python"]
deprecated_since: "Python 3.3"
---

# [Solution] Deprecated Function Migration: logging.warn() to logging.warning()

The `logging.warn()` has been deprecated in favor of `logging.warning()`.

## Migration Guide

logging.warn() has been deprecated since Python 3.3 in favor of logging.warning(). The warn method emits a DeprecationWarning.

## Before (Deprecated)

```python
import logging

logging.warn("This is a warning")
logging.warn("Disk space low: %s%%", usage)
```

## After (Modern)

```python
import logging

logging.warning("This is a warning")
logging.warning("Disk space low: %s%%", usage)
```

## Key Differences

- Simple rename from warn to warning
- Same signature and behavior
- Run grep -rn 'logging.warn(' to find instances

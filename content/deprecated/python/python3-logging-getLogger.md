---
title: "[Solution] Deprecated Function Migration: logging root logger to named loggers"
description: "Migrate from deprecated root logger usage to named loggers."
deprecated_function: "logging.info(msg)"
replacement_function: "logging.getLogger(__name__)"
languages: ["python"]
deprecated_since: "Python 2.6+"
---

# [Solution] Deprecated Function Migration: logging root logger to named loggers

The `logging.info(msg)` has been deprecated in favor of `logging.getLogger(__name__)`.

## Migration Guide

Named loggers provide better filtering and organization

Using root logger directly loses module context.

## Before (Deprecated)

```python
import logging
logging.info("Starting process")
```

## After (Modern)

```python
import logging
logger = logging.getLogger(__name__)
logger.info("Starting process")
```

## Key Differences

- Named loggers provide module context
- Better filtering by logger name
- Hierarchical logger structure
- Each module gets its own logger

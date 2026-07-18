---
title: "[Solution] Python Logging Configuration Error — How to Fix"
description: "Fix Python logging errors. Resolve handler, formatter, and configuration issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Logging Configuration Error

A `ValueError: I/O operation on closed file` occurs when Logging module fails to write messages due to handler misconfiguration or encoding issues..

## Why It Happens

This happens when handlers have conflicting configurations, loggers have circular references, or encoding fails. Python enforces strict type and state checking.

## Common Error Messages

- `I/O operation on closed file`
- `UnicodeEncodeError: 'ascii' codec`
- `maximum recursion depth exceeded`

## How to Fix It

### Fix 1: Configure handlers

```python
import logging
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
```

### Fix 2: Fix encoding

```python
handler = logging.FileHandler('app.log', encoding='utf-8')
```

### Fix 3: dictConfig

```python
import logging.config
config = {'version': 1, 'handlers': {'file': {'class': 'logging.FileHandler', 'filename': 'app.log'}}, 'root': {'level': 'DEBUG', 'handlers': ['file']}}
logging.config.dictConfig(config)
```

### Fix 4: Avoid duplicates

```python
def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    return logger
```

## Common Scenarios

- **Log rotation** — Unbounded log files grow without limit.
- **Performance** — Synchronous logging blocks main thread.
- **Thread safety** — Multiple threads writing to same handler.

## Prevent It

- Check if logger has handlers before adding
- Use RotatingFileHandler for rotation
- Set dictConfig at application startup

## Related Errors

- - [ValueError](/languages/python/valueerror/) — invalid argument
- - [OSError](/languages/python/oserror/) — system call error

---
title: "[Solution] Python Loguru Error — Logging Framework Failures"
description: "Fix Python Loguru errors like logger configuration, sink errors, format errors, and rotation errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 433
---

# Python Loguru Error — Logging Framework Failures

Loguru errors occur when logger sinks are misconfigured, format strings are invalid, rotation settings are incorrect, or file paths are inaccessible. These are common in production logging setups.

## Common Causes

```python
# ValueError: invalid sink
from loguru import logger
logger.add(12345)  # sink must be str, Path, file object, or callable

# FileNotFoundError: log directory doesn't exist
from loguru import logger
logger.add("/nonexistent/path/app.log")

# FormatError: invalid format string
from loguru import logger
logger.add("app.log", format="{invalid_field} {message}")

# ValueError: rotation configuration invalid
from loguru import logger
logger.add("app.log", rotation="invalid_value")

# TypeError: sink is not callable
from loguru import logger
logger.add(lambda msg: print(msg), format=12345)  # format must be str
```

## How to Fix

### Fix 1: Use Valid Sink Types
Provide a valid sink: file path, callable, or file-like object.
```python
from loguru import logger
import sys

# File sink
logger.add("app.log")

# Stderr sink (default)
logger.add(sys.stderr)

# Callable sink
logger.add(lambda msg: print(msg, end=""))

# Async sink
async def async_sink(message):
    await send_to_service(message)

logger.add(async_sink)
```

### Fix 2: Ensure Log Directory Exists
Create the directory before adding a file sink.
```python
from loguru import logger
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

logger.add(log_dir / "app.log", rotation="10 MB")
```

### Fix 3: Use Valid Format Strings
Use Loguru's built-in format fields.
```python
from loguru import logger

# Valid format fields: time, level, message, name, function, line, etc.
logger.add(
    "app.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
)
```

### Fix 4: Configure Rotation Correctly
Use valid rotation configuration values.
```python
from loguru import logger

# Rotate by size
logger.add("app.log", rotation="10 MB")

# Rotate by time
logger.add("app.log", rotation="00:00")  # midnight
logger.add("app.log", rotation="1 week")

# Rotate by function
logger.add("app.log", rotation=lambda msg: msg["time"].day == 1)  # monthly
```

### Fix 5: Remove and Reconfigure Logger
Properly reset the logger before reconfiguration.
```python
from loguru import logger
import sys

# Remove all handlers
logger.remove()

# Add new configuration
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}",
    level="INFO",
    colorize=True,
)

logger.add(
    "app.log",
    rotation="50 MB",
    retention="30 days",
    compression="zip",
    level="DEBUG",
)
```

## Examples

```python
# Production logging configuration
from loguru import logger
import sys
from pathlib import Path

def setup_logging():
    logger.remove()  # Remove default handler

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Console output
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True,
    )

    # File output with rotation
    logger.add(
        log_dir / "app_{time:YYYY-MM-DD}.log",
        rotation="00:00",
        retention="30 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
        level="DEBUG",
    )

    # Error-only file
    logger.add(
        log_dir / "errors.log",
        rotation="10 MB",
        retention="90 days",
        level="ERROR",
    )

setup_logging()
logger.info("Logging configured")
```

## Related Errors

- [Python pytest Error](/languages/python/python-pytest-error-extended/)
- [Python Pydantic Error](/languages/python/python-pydantic-error/)
- [Python FastAPI Error](/languages/python/python-fastapi-error/)

---
title: "[Solution] Python Loguru Logging Error — How to Fix"
description: "Fix Python Loguru logging errors. Resolve sink configuration issues, rotation failures, and exception formatting problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Loguru Logging Error

A `loguru._recattrs.LoguruException` or `TypeError` occurs when Loguru fails to configure a sink, encounters invalid rotation parameters, or cannot serialize exception context due to missing dependencies.

## Why It Happens

Loguru replaces Python's standard logging with a simpler API. Errors arise when sinks are not callable, rotation functions return invalid values, exception formatting requires unavailable packages, or file paths are not writable.

## Common Error Messages

- `TypeError: sink must be callable or file-like object`
- `ValueError: rotation time must be a positive integer`
- `FileNotFoundError: [Errno 2] No such file or directory: 'logs/app.log'`
- `UnicodeEncodeError: 'utf-8' codec can't encode character`

## How to Fix It

### Fix 1: Configure sinks correctly

```python
from loguru import logger

# Wrong — passing non-callable as sink
# logger.add(123)  # TypeError

# Correct — use valid sink types
import sys

# File sink
logger.add("logs/app.log", rotation="10 MB", retention="30 days")

# Stream sink
logger.add(sys.stderr, level="INFO")

# Callable sink
def custom_sink(message):
    print(f"CUSTOM: {message}")

logger.add(custom_sink, format="{time} {level} {message}")
logger.info("Application started")
```

### Fix 2: Fix rotation configuration

```python
from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

# Wrong — invalid rotation value
# logger.add("logs/app.log", rotation="invalid")

# Correct — use proper rotation types
# Time-based rotation
logger.add("logs/daily.log", rotation="00:00")  # midnight
logger.add("logs/hourly.log", rotation="1 hour")

# Size-based rotation
logger.add("logs/size.log", rotation="10 MB")

# Custom rotation function
def my_rotation(message):
    return message.record["time"].day == 1  # rotate on first of month

logger.add("logs/custom.log", rotation=my_rotation)

# Retention policy
logger.add("logs/retained.log", rotation="10 MB", retention="7 days")
```

### Fix 3: Handle exception formatting

```python
from loguru import logger

# Wrong — missing dependencies for enhanced formatting
# logger.add("app.log", backtrace=True, diagnose=True)
# may fail if exceptions groups not available

# Correct — configure exception handling safely
import sys

logger.add(
    sys.stderr,
    backtrace=True,
    diagnose=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} | {message}",
)

try:
    result = 1 / 0
except Exception:
    logger.exception("Division by zero occurred")
```

### Fix 4: Manage log levels and filters

```python
from loguru import logger
import sys

# Wrong — all messages go to same sink
# logger.add("app.log")
# logger.info("debug message")  # logged even at INFO level

# Correct — filter by level and context
logger.add(
    "logs/error.log",
    level="ERROR",
    rotation="10 MB",
    filter=lambda record: record["extra"].get("module") == "auth",
)

logger.add(
    sys.stderr,
    level="DEBUG",
    format="<green>{time}</green> <level>{level}</level> <cyan>{name}</cyan> {message}",
)

# Bind context to loggers
auth_log = logger.bind(module="auth")
auth_log.info("Login attempt", user_id=123)
auth_log.error("Authentication failed")

# Unbind to remove context
clean_log = auth_log.unbind("module")
clean_log.info("General message")
```

## Common Scenarios

- **Sink not callable** — Passing a string or integer directly as a sink instead of using it as a file path or callable.
- **Log directory missing** — Writing to a log file in a directory that does not exist causes FileNotFoundError.
- **Rotation conflict** — Using both time-based and size-based rotation in the same sink configuration.

## Prevent It

- Always create log directories with `os.makedirs()` before configuring file sinks.
- Use `logger.level()` to define custom levels before filtering on them.
- Test logging configuration with `logger.info()` at application startup to catch sink issues early.

## Related Errors

- [FileNotFoundError](/languages/python/filenotfounderror/) — log directory does not exist
- [TypeError](/languages/python/typeerror/) — invalid sink type
- [ValueError](/languages/python/valueerror/) — invalid rotation parameter

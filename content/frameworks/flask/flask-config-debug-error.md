---
title: "[Solution] Flask Config Debug Error"
description: "Fix Flask debug configuration errors when debug mode causes issues or fails to enable properly."
frameworks: ["flask"]
error-types: ["configuration-error"]
severities: ["error"]
---

Flask debug configuration errors occur when debug mode is not properly enabled, causing the debugger not to work or security issues in production.

## Common Causes

- `DEBUG` not set in configuration
- Debug mode enabled in production (security risk)
- Debugger PIN not configured
- Reloader conflicts with application code
- Debug mode affects performance significantly

## How to Fix

### Configure Debug Mode Properly

```python
import os
from flask import Flask

app = Flask(__name__)

# Only enable debug in development
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-key")
```

### Use Environment Variables

```bash
# Development
export FLASK_DEBUG=1
flask run

# Production
export FLASK_DEBUG=0
flask run
```

### Configure Debugger PIN

```python
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
```

## Examples

```python
import os
from flask import Flask

app = Flask(__name__)

# Bug -- debug enabled unconditionally
app.config["DEBUG"] = True  # Security risk in production

# Fix -- use environment variable
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "false") == "true"
```

Never enable debug mode in production as it exposes the interactive debugger.

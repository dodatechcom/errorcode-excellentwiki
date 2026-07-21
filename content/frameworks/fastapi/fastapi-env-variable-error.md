---
title: "[Solution] FastAPI Environment Variable Error"
description: "Fix FastAPI environment variable errors when configuration values are missing or have incorrect types."
frameworks: ["fastapi"]
error-types: ["configuration-error"]
severities: ["error"]
---

When FastAPI relies on environment variables for configuration, missing or malformed values cause startup failures.

## Common Causes

- Environment variable not set before application starts
- Variable contains spaces or special characters not properly quoted
- Type conversion fails (e.g., `int("not-a-number")`)
- `.env` file not loaded by `python-dotenv`
- Variable name has a typo or inconsistent casing

## How to Fix

### Use Pydantic Settings for Validation

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    port: int = 8000

    model_config = {"env_file": ".env"}

settings = Settings()
```

### Load Environment Variables Manually

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
PORT = int(os.getenv("PORT", "8000"))
```

### Validate Required Variables

```python
import os

required = ["DATABASE_URL", "SECRET_KEY", "REDIS_URL"]
missing = [var for var in required if not os.getenv(var)]
if missing:
    raise RuntimeError(f"Missing required env vars: {', '.join(missing)}")
```

## Examples

```python
import os

# Bug -- no default, crashes if not set
db_url = os.environ["DATABASE_URL"]  # KeyError if missing

# Fix -- use getenv with default
db_url = os.getenv("DATABASE_URL", "sqlite:///default.db")
```

Create a `.env` file:

```
DATABASE_URL=postgresql://user:pass@localhost/db
SECRET_KEY=my-secret-key
DEBUG=true
```

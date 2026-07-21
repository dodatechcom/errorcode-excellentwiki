---
title: "[Solution] FastAPI Config Values Error"
description: "Fix FastAPI configuration values errors when settings are missing, duplicated, or have conflicting values."
frameworks: ["fastapi"]
error-types: ["configuration-error"]
severities: ["error"]
---

When FastAPI applications use multiple configuration sources, conflicting or missing values cause unpredictable behavior.

## Common Causes

- Environment variable overrides `.env` file value unexpectedly
- Pydantic settings model has wrong default values
- Configuration loaded before `.env` file is read
- Multiple configuration files with overlapping keys
- Type conversion fails for numeric or boolean config values

## How to Fix

### Define Clear Configuration Hierarchy

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///default.db"
    debug: bool = False
    api_key: str = ""

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
    }

settings = Settings()
```

### Load Configuration at Application Start

```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = Settings()
    app.state.settings = settings
    yield

app = FastAPI(lifespan=lifespan)
```

### Validate Required Configuration

```python
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    redis_url: str = "redis://localhost:6379/0"
```

## Examples

```python
from pydantic_settings import BaseSettings

# Env vars take precedence over .env file
# If .env has DEBUG=true and env var DEBUG=false, result is False
```

Set configuration values in order of precedence:
1. Environment variables (highest priority)
2. `.env` file
3. Default values in the model (lowest priority)

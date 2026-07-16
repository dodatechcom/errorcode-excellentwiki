---
title: "Config error: key not set"
description: "Flask raises RuntimeError or AttributeError when a required configuration key is missing"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["config", "configuration", "secret-key", "settings"]
weight: 5
---

This error occurs when Flask cannot find a required configuration key. This commonly happens with `SECRET_KEY`, database URLs, or other critical settings that are expected but not loaded.

## Common Causes

- `SECRET_KEY` not set or not loaded from environment
- Environment variable not available in the deployment environment
- Missing `.env` file or `python-dotenv` not loaded
- Configuration class or file not properly imported

## How to Fix

1. Load configuration from environment variables:

```python
import os

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-me')
```

2. Use `python-dotenv` to load a `.env` file:

```python
from dotenv import load_dotenv
import os

load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

3. Load from a Python config file:

```python
app.config.from_object('config.ProductionConfig')
```

4. Use a separate config class:

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProductionConfig(Config):
    DEBUG = False

app.config.from_object(ProductionConfig)
```

## Examples

```python
app = Flask(__name__)

@app.route('/secret')
def secret():
    return app.config['SECRET_KEY']  # KeyError if not set
```

```text
KeyError: 'SECRET_KEY'
```

## Related Errors

- [Blueprint registration error]({{< relref "/frameworks/flask/blueprint-error" >}})

---
title: "[Solution] Python ImportError: No module named 'flask' — Fix"
description: "Fix Python ImportError: No module named 'flask'. Install Flask with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 318
---

# Python ImportError: No module named 'flask'

Flask is a lightweight WSGI web application framework for Python. This error appears when the `flask` package is missing from the active Python environment.

## Common Causes

```python
# Cause 1: Flask not installed
from flask import Flask  # ImportError: No module named 'flask'

# Cause 2: Wrong virtual environment
# Flask installed in venv but system Python is being used

# Cause 3: Case-sensitive import
import Flask  # ImportError — must be lowercase 'flask'

# Cause 4: Flask installed for different Python interpreter
pip install flask  # installs for python3 but you run python3.12

# Cause 5: Outdated pip cannot find the package
pip install flask  # Could not find a version
```

## How to Fix

### Fix 1: Install Flask with pip

```bash
pip install flask

# For a specific version
pip install flask==3.0.2

# With common extensions
pip install flask flask-sqlalchemy flask-migrate
```

### Fix 2: Activate virtual environment first

```bash
source venv/bin/activate
pip install flask
python -c "import flask; print(flask.__version__)"
```

### Fix 3: Upgrade pip and retry

```bash
pip install --upgrade pip
pip install flask
```

## Examples

```python
# Minimal Flask app after installation
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

## Related Errors

- {{< relref "importerror-flask2" >}} — ImportError: flask (variant)
- {{< relref "importerror-flask-sqlalchemy" >}} — ImportError: flask_sqlalchemy
- {{< relref "importerror-gunicorn" >}} — ImportError: gunicorn

---
title: "[Solution] Python ImportError: No module named 'flask_sqlalchemy' — Fix"
description: "Fix Python ImportError: No module named 'flask_sqlalchemy'. Install Flask-SQLAlchemy with pip and resolve dependency conflicts."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 309
---

# Python ImportError: No module named 'flask_sqlalchemy'

The `ModuleNotFoundError: No module named 'flask_sqlalchemy'` error occurs when Python cannot locate the Flask-SQLAlchemy package, which integrates SQLAlchemy with the Flask web framework.

## Common Causes

```python
# Cause 1: Flask-SQLAlchemy not installed
from flask_sqlalchemy import SQLAlchemy  # ModuleNotFoundError

# Cause 2: Installed for wrong Python version or virtual environment
import flask_sqlalchemy  # ModuleNotFoundError

# Cause 3: Package name vs import name mismatch
# pip install Flask-SQLAlchemy → import flask_sqlalchemy
```

```python
# Cause 4: Flask installed but Flask-SQLAlchemy missing
# pip install flask does not include Flask-SQLAlchemy

# Cause 5: SQLAlchemy version conflict
# Flask-SQLAlchemy requires specific SQLAlchemy version range
```

## How to Fix

### Fix 1: Install Flask-SQLAlchemy with pip

```bash
pip install Flask-SQLAlchemy

# Verify installation
python -c "import flask_sqlalchemy; print(flask_sqlalchemy.__version__)"
```

### Fix 2: Install in the correct virtual environment

```bash
source venv/bin/activate
pip install Flask-SQLAlchemy
python -c "from flask_sqlalchemy import SQLAlchemy; print('OK')"
```

### Fix 3: Add to project requirements

```bash
# requirements.txt
Flask
Flask-SQLAlchemy

# Install
pip install -r requirements.txt
```

## Examples

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
```

```bash
# Initialize database
flask shell
>>> from app import db
>>> db.create_all()
```

## Related Errors

- {{< relref "importerror-flask2" >}} — ImportError: flask
- {{< relref "importerror-sqlalchemy" >}} — ImportError: sqlalchemy
- {{< relref "importerror-alembic" >}} — ImportError: alembic

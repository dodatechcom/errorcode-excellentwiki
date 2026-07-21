---
title: "[Solution] Flask Template Not Found Error"
description: "Fix Flask template not found errors when Jinja2 cannot locate or render template files."
frameworks: ["flask"]
error-types: ["template-error"]
severities: ["error"]
---

Template not found errors occur when Flask cannot locate the template file in the expected directory.

## Common Causes

- Template file does not exist in the templates folder
- Template folder path is incorrect
- Template name includes wrong extension
- Blueprint template folder not configured
- Case sensitivity in template names (Linux)

## How to Fix

### Verify Template Location

```
app/
  templates/
    base.html
    index.html
    errors/
      404.html
      500.html
```

### Configure Template Folder

```python
from flask import Flask

app = Flask(__name__, template_folder="templates")

# Or for blueprints
api_bp = Blueprint("api", __name__, template_folder="api_templates")
```

### Use Correct Template Name

```python
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")  # Not "templates/index.html"
```

### Handle Missing Templates

```python
from flask import render_template
from jinja2 import TemplateNotFound

@app.route("/")
def index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return render_template("fallback.html")
```

## Examples

```python
from flask import Flask, render_template

app = Flask(__name__)

# Bug -- wrong template path
@app.route("/")
def index():
    return render_template("templates/index.html")  # Wrong!

# Fix -- correct template name
@app.route("/")
def index_fixed():
    return render_template("index.html")
```

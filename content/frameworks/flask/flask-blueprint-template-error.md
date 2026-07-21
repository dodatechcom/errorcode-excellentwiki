---
title: "[Solution] Flask Blueprint Template Error"
description: "Fix Flask blueprint template errors when templates are not found or rendered incorrectly in blueprints."
frameworks: ["flask"]
error-types: ["template-error"]
severities: ["error"]
---

Blueprint template errors occur when Flask cannot locate templates because the template folder path is incorrect or the blueprint is not properly configured.

## Common Causes

- Blueprint template folder not specified
- Template path relative to wrong directory
- Template name conflicts between blueprints
- Template folder does not exist
- Jinja2 template syntax errors

## How to Fix

### Configure Blueprint Template Folder

```python
from flask import Blueprint, render_template

main_bp = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@main_bp.route("/")
def index():
    return render_template("main/index.html")
```

### Use Namespaced Templates

```
app/
  templates/
    main/
      index.html
      about.html
    api/
      data.html
```

### Avoid Template Name Conflicts

```python
# Use unique template names per blueprint
main_bp = Blueprint("main", __name__, template_folder="templates/main")
api_bp = Blueprint("api", __name__, template_folder="templates/api")
```

## Examples

```python
from flask import Blueprint, render_template

app_bp = Blueprint("app", __name__, template_folder="templates")

# Bug -- template not in blueprint folder
@app_bp.route("/test")
def test():
    return render_template("wrong_path.html")  # TemplateNotFound

# Fix -- correct template path
@app_bp.route("/test-fixed")
def test_fixed():
    return render_template("app/test.html")
```

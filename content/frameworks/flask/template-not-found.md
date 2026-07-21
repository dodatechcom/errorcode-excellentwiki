---
title: "TemplateNotFound: X.html"
description: "Flask raises TemplateNotFound when Jinja2 cannot locate the requested template file."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Flask's Jinja2 template loader cannot find the template file you passed to `render_template()`. The file may be missing, misplaced, or named incorrectly.

## Common Causes

- Template file does not exist in the `templates/` folder
- Filename typo or wrong file extension (e.g. `.htm` vs `.html`)
- Using a subdirectory without including it in the path (e.g. `admin/dashboard.html` instead of `dashboard.html`)
- Custom template folder configured but not set correctly in the Flask app

## How to Fix

Make sure the template exists in the expected location. Flask looks in the `templates/` folder by default:

```
myapp/
├── app.py
└── templates/
    └── index.html
```

If you use a custom template folder, configure it explicitly:

```python
app = Flask(__name__, template_folder="custom_templates")
```

Check the path you pass to `render_template`:

```python
# Wrong -- file is in templates/admin/
render_template("dashboard.html")

# Correct
render_template("admin/dashboard.html")
```

## Example

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")  # home.html does not exist
```

```text
jinja2.exceptions.TemplateNotFound: home.html
```

## Related Errors

- [ImportError: cannot import name 'X']({{< relref "/frameworks/flask/import-error" >}})

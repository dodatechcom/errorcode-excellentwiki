---
title: "[Solution] Flask Template Inheritance Error"
description: "Fix Flask template inheritance errors when child templates do not properly extend parent templates."
frameworks: ["flask"]
error-types: ["template-error"]
severities: ["error"]
---

Template inheritance errors occur when child templates do not correctly override blocks or when the parent template structure is wrong.

## Common Causes

- `{% extends %}` tag not at the beginning of the template
- Block names do not match between parent and child
- Child template has content outside of blocks
- Parent template uses `{% block %}` without `{% endblock %}`
- Recursive template inclusion

## How to Fix

### Use Proper Template Structure

```html
{# base.html #}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### Override Blocks in Child Templates

```html
{# child.html #}
{% extends "base.html" %}

{% block title %}Custom Title{% endblock %}

{% block content %}
<h1>Welcome</h1>
{% endblock %}
```

### Use Template Inheritance with Blueprints

```python
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__, template_folder="templates")

@main_bp.route("/")
def index():
    return render_template("main/index.html")
```

## Examples

```html
{# Bug -- content outside blocks #}
{% extends "base.html" %}
<h1>This will not render</h1>
{% block content %}Only this renders{% endblock %}

{# Fix -- put all content in blocks #}
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
<h1>This renders correctly</h1>
{% endblock %}
```

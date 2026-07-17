---
title: "Jinja2 Template Error in Flask"
description: "Flask raises TemplateError when rendering a Jinja2 template with invalid syntax, undefined variables, or incorrect filters"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jinja2", "template", "rendering", "syntax", "flask"]
weight: 5
---

## What This Error Means

A Jinja2 template error in Flask occurs when the template engine encounters invalid syntax, references an undefined variable, or uses an incorrect filter. Flask uses Jinja2 as its default template engine, and template errors are raised during `render_template()` calls.

## Common Causes

- Undefined variable passed to template (missing from render context)
- Invalid Jinja2 syntax (mismatched `{% if %}` / `{% endif %}`)
- Accessing attribute on `None` value in template
- Inconsistent template inheritance (missing `{% extends %}`)

## How to Fix

Use `undefined` variable handling in templates:

```html
<!-- Jinja2: safe access with default -->
{{ user.name if user else "Anonymous" }}
```

Use the `set` tag for default values:

```html
{% set username = user.name if user else "Guest" %}
<p>Welcome, {{ username }}</p>
```

Pass all required variables from the view:

```python
@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(author_id=user.id).all()
    return render_template("profile.html", user=user, posts=posts)
```

Use `strictundefined` for cleaner error messages in development:

```python
from jinja2 import StrictUndefined
app.jinja_env.undefined = StrictUndefined
```

## Examples

```python
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")  # missing 'user'
```

```html
<!-- dashboard.html -->
<h1>Welcome, {{ user.name }}</h1>
```

```text
jinja2.exceptions.UndefinedError: 'user' is undefined
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [Import error]({{< relref "/frameworks/flask/import-error" >}})

---
title: "Jinja2 template error"
description: "Flask raises TemplateError or TemplateSyntaxError when rendering a Jinja2 template with invalid syntax or undefined variables"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["jinja2", "template", "rendering", "syntax"]
weight: 5
---

This error occurs when Jinja2 encounters an invalid template syntax or tries to render a variable that is not defined. Flask uses Jinja2 as its default template engine.

## Common Causes

- Undefined variable passed to template (missing from render context)
- Invalid Jinja2 syntax (mismatched `{% if %}` / `{% endif %}`)
- Accessing attribute on `None` value in template
- Inconsistent template inheritance (missing `{% extends %}`)

## How to Fix

1. Use `undefined` variable handling in templates:

```html
<!-- Jinja2: safe access with default -->
{{ user.name if user else "Anonymous" }}
```

2. Use the `set` tag for default values:

```html
{% set username = user.name if user else "Guest" %}
<p>Welcome, {{ username }}</p>
```

3. Pass all required variables from the view:

```python
def profile(user_id):
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(author_id=user.id).all()
    return render_template("profile.html", user=user, posts=posts)
```

4. Use `strictundefined` for cleaner error messages in development:

```python
app.jinja_env.undefined = StrictUndefined
```

## Examples

```python
@app.route('/profile')
def profile():
    return render_template("profile.html")  # missing 'user'
```

```html
<!-- profile.html -->
<h1>{{ user.name }}</h1>
```

```text
jinja2.exceptions.UndefinedError: 'user' is undefined
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})

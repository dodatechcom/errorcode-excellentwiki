---
title: "Flask-WTF Form Error"
description: "Flask-WTF raises validation errors when form data fails validation checks or CSRF token is missing"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["wtf", "form", "validation", "csrf", "flask"]
weight: 5
---

## What This Error Means

Flask-WTF form errors occur when form validation fails, CSRF protection rejects a request, or form fields do not meet validation criteria. These errors manifest as `ValidationError` on individual fields or `CSRFError` when the CSRF token is invalid or missing.

## Common Causes

- Form field fails validation (required field empty, invalid format)
- CSRF token missing or invalid in submitted form
- Form submitted without proper `enctype`
- Custom validator raising `ValidationError`
- JavaScript form submission bypassing CSRF token

## How to Fix

Handle form validation in your view:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Process valid form data
        send_email(form.email.data, form.name.data)
        return redirect(url_for('success'))
    return render_template('contact.html', form=form)
```

Ensure CSRF token is included in your template:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.name.label }} {{ form.name() }}
    {{ form.email.label }} {{ form.email() }}
    <button type="submit">Submit</button>
</form>
```

Display validation errors in your template:

```html
<form method="POST">
    {{ form.hidden_tag() }}
    {% for field in form %}
        {{ field.label }}
        {{ field() }}
        {% for error in field.errors %}
            <span class="error">{{ error }}</span>
        {% endfor %}
    {% endfor %}
    <button type="submit">Submit</button>
</form>
```

Disable CSRF for API endpoints:

```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)

@app.route('/api/submit', methods=['POST'])
@csrf.exempt
def api_submit():
    data = request.get_json()
    return jsonify({'status': 'ok'})
```

## Examples

```python
form = ContactForm()
if not form.validate():
    print(form.errors)
# {'email': ['Invalid email address.'], 'name': ['This field is required.']}
```

```text
flask_wtf.csrf.CSRFError: 400 Bad Request: The CSRF token is missing.
```

## Related Errors

- [Template error]({{< relref "/frameworks/flask/jinja-error" >}})
- [Session error]({{< relref "/frameworks/flask/session-error" >}})

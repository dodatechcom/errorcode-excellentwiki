---
title: "Flask-Login Authentication Error"
description: "Flask-Login raises errors related to user authentication, session management, and access control"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Login errors occur when the authentication system cannot properly manage user sessions, load user objects, or enforce access control. Common errors include `UserNotFoundError`, unauthorized access attempts, and missing user loader configuration.

## Common Causes

- Missing `@login_manager.user_loader` callback
- User not implementing `UserMixin` or required methods
- Session expired or cookie not set
- Protected route accessed without authentication
- User ID not found in database

## How to Fix

Define the user loader callback:

```python
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

Implement `UserMixin` in your user model:

```python
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(120))
```

Protect routes with `@login_required`:

```python
from flask_login import login_required, current_user

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)
```

Handle unauthorized access redirects:

```python
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
```

## Examples

```python
@app.route('/admin')
@login_required
def admin():
    return 'Admin panel'
```

```text
werkzeug.exceptions.Unauthorized: 401 Unauthorized
```

## Related Errors

- [Session error]({{< relref "/frameworks/flask/session-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})

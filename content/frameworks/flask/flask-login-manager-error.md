---
title: "[Solution] Flask Login Manager Error"
description: "Fix Flask Login Manager errors when user authentication or session management fails."
frameworks: ["flask"]
error-types: ["authentication-error"]
severities: ["error"]
---

Flask-Login manager errors occur when the user loader callback fails, session management is misconfigured, or authentication state is inconsistent.

## Common Causes

- `user_loader` callback not registered
- User loader returns `None` for valid user IDs
- Session not configured with proper secret key
- `remember_token` cookie conflicts with session-based auth
- User model does not inherit `UserMixin`

## How to Fix

### Configure Login Manager

```python
from flask import Flask
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/login", methods=["POST"])
def login():
    user = User.query.filter_by(username=request.form["username"]).first()
    if user and user.check_password(request.form["password"]):
        login_user(user)
        return redirect(url_for("dashboard"))
    return "Invalid credentials", 401
```

### Handle Missing User Loader

```python
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    if user is None:
        return None  # Flask-Login will handle this
    return user
```

## Examples

```python
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)

# Bug -- no user_loader registered
# This causes "UserLoader" error on login

# Fix
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

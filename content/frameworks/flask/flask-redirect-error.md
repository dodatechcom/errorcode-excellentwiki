---
title: "[Solution] Flask Redirect Loop Detected Error — How to Fix"
description: "Fix Flask redirect loop errors. Resolve infinite redirect cycles, URL redirect issues in Flask applications."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask redirect loop detected error occurs when a series of redirects cycles back to the starting URL, causing the browser to give up. This is commonly caused by conflicting decorators, misconfigured login requirements, or circular URL rules.

## Why It Happens

Redirect loops happen when route A redirects to route B, which redirects back to route A. Common causes include `@login_required` decorators redirecting to a login page that itself requires authentication, conflicting before_request hooks, middleware that redirects based on conditions that are always true, or URL rules that point to each other.

## Common Error Messages

```
ERR_TOO_MANY_REDIRECTS
```

```
The page isn't working — redirected you too many times
```

```
RuntimeError: Redirect loop detected
```

```
werkzeug.exceptions.TooManyRedirects: 308 Too Many Redirects
```

## How to Fix It

### 1. Fix Login Required Redirect Loops

Ensure the login route is accessible without authentication:

```python
from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_required

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'  # Where to redirect unauthenticated users

@app.route('/login')
def login():
    # This route must NOT have @login_required
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Make sure the login page doesn't redirect to itself
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))
```

### 2. Check before_request Hooks

Ensure `before_request` doesn't redirect unnecessarily:

```python
@app.before_request
def check_maintenance():
    # Bad: always redirects, even for login page
    # if not is_admin():
    #     return redirect(url_for('maintenance'))

    # Good: exclude login and static files
    if request.endpoint in ('login', 'static'):
        return None
    if not is_admin():
        return redirect(url_for('maintenance'))
```

### 3. Fix URL Rule Conflicts

Ensure `redirect()` and `url_for()` don't create cycles:

```python
@app.route('/old-page')
def old_page():
    # Redirect to the new URL
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return "This is the new page"

# Never do this — it creates a loop
# @app.route('/a')
# def a():
#     return redirect(url_for('b'))
# @app.route('/b')
# def b():
#     return redirect(url_for('a'))
```

### 4. Debug Redirect Loops

Use curl to trace redirect chains:

```bash
# Follow redirects and show each hop
curl -v -L http://localhost:5000/old-page 2>&1 | grep -i "location:"

# Or use Python requests
python3 -c "
import requests
try:
    r = requests.get('http://localhost:5000/', allow_redirects=True)
    print(f'Final status: {r.status_code}')
    print(f'History: {[h.url for h in r.history]}')
except requests.exceptions.TooManyRedirects:
    print('Redirect loop detected!')
"
```

## Common Scenarios

**Scenario 1: Redirect loop after deploying with HTTPS.**
If your proxy handles HTTPS but Flask sees HTTP, `url_for()` generates HTTP URLs while the browser expects HTTPS. Set `PREFERRED_URL_SCHEME`:

```python
app.config['PREFERRED_URL_SCHEME'] = 'https'
```

**Scenario 2: Redirect loop with `next` parameter.**
When the login page saves a `next` URL but redirects to itself:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ... authenticate user ...
        next_url = request.args.get('next', url_for('dashboard'))
        return redirect(next_url)
    return render_template('login.html')
```

**Scenario 3: Redirect loop with extensions.**
Some Flask extensions add `before_request` hooks that redirect. Check extension documentation and exclude certain routes from processing.

## Prevent It

1. **Always test redirect chains.** Use browser developer tools to inspect the redirect chain and identify where the loop starts.

2. **Exclude authentication pages from redirects.** Login, logout, and password reset routes should always be accessible.

3. **Use `curl -v -L` during development** to trace redirect chains and catch loops before they reach production.

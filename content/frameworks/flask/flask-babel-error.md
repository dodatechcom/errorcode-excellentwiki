---
title: "Flask-Babel i18n Error"
description: "Flask-Babel raises errors when internationalization or translation operations fail"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["babel", "i18n", "translation", "locale", "flask"]
weight: 5
---

## What This Error Means

Flask-Babel errors occur when internationalization (i18n) or translation operations fail due to missing locale files, incorrect translation IDs, or configuration issues. These errors manifest as missing translations or locale resolution failures.

## Common Causes

- Translation catalog not compiled or missing
- Locale not set or resolved correctly
- Missing `gettext` calls in templates
- Incorrect `.po` file formatting
- Babel extraction not run after source changes

## How to Fix

Configure Flask-Babel:

```python
from flask_babel import Babel, gettext as _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)
```

Use translation functions in templates:

```html
<h1>{{ _('Welcome to our application') }}</h1>
<p>{{ _('You have %(count)s notifications', count=unread_count) }}</p>
```

Extract translation strings:

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel init -i messages.pot -d translations -l fr
pybabel compile -d translations
```

Handle missing translations gracefully:

```python
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['en', 'fr', 'de'], 'en')
```

Update translations after source changes:

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
pybabel compile -d translations
```

## Examples

```python
@app.route('/hello')
def hello():
    return _('Hello, World!')
```

```text
jinja2.exceptions.UndefinedError: '_' is undefined
```

## Related Errors

- [Template error]({{< relref "/frameworks/flask/jinja-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})

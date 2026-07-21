---
title: "[Solution] Flask Render Template Error"
description: "render_template failing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

render_template failing.

## Common Causes

Wrong name.

## How to Fix

Pass correct name.

## Example

```python
@app.route('/p')
def p(): return render_template('page.html', name='World')
```

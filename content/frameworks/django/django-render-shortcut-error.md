---
title: "[Solution] Django Render Shortcut Error"
description: "render() template not found."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

render() template not found.

## Common Causes

Wrong name.

## How to Fix

Check path.

## Example

```python
from django.shortcuts import render
return render(request, 'myapp/page.html', {'d': data})
```

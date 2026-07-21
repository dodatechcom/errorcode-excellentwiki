---
title: "[Solution] Django Template Loaders Error"
description: "Template loaders not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Template loaders not working.

## Common Causes

Wrong loaders.

## How to Fix

Configure loaders.

## Example

```python
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'OPTIONS': {'loaders': ['django.template.loaders.filesystem.Loader']}}]
```

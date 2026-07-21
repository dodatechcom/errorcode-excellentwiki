---
title: "[Solution] Django Pagination Error REST"
description: "Pagination not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Pagination not working.

## Common Causes

Not configured.

## How to Fix

Configure.

## Example

```python
REST_FRAMEWORK = {'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', 'PAGE_SIZE': 10}
```

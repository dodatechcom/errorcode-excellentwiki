---
title: "[Solution] Django Test Mock Error"
description: "Test mock not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Test mock not working.

## Common Causes

Wrong mock.

## How to Fix

Use unittest.mock.

## Example

```python
from unittest.mock import patch
@patch('myapp.views.get_data')
def test(mock):
    mock.return_value = []
```

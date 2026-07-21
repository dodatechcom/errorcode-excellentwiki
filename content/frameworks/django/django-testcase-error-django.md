---
title: "[Solution] Django TestCase Error Django"
description: "TestCase not running."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

TestCase not running.

## Common Causes

Wrong setup.

## How to Fix

Use TestCase.

## Example

```python
from django.test import TestCase
class MyTest(TestCase):
    def test_something(self):
        self.assertEqual(1 + 1, 2)
```

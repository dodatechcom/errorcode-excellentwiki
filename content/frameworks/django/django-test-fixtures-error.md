---
title: "[Solution] Django Test Fixtures Error"
description: "Test fixtures not loading."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Test fixtures not loading.

## Common Causes

Wrong fixture.

## How to Fix

Use correct fixture.

## Example

```python
class MyTest(TestCase):
    fixtures = ['test_data.json']
```

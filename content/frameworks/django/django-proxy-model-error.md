---
title: "[Solution] Django Proxy Model Error"
description: "Proxy model not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Proxy model not working.

## Common Causes

Not proxy.

## How to Fix

Set proxy.

## Example

```python
class ActiveUser(User):
    class Meta:
        proxy = True
    def active_posts(self):
        return self.posts.filter(active=True)
```

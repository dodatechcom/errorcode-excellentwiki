---
title: "[Solution] Django Signal Receive Error"
description: "Signal receiver not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Signal receiver not working.

## Common Causes

Wrong decorator.

## How to Fix

Use @receiver.

## Example

```python
from django.dispatch import receiver
@receiver(post_save, sender=User)
def handler(sender, instance, **kwargs): pass
```

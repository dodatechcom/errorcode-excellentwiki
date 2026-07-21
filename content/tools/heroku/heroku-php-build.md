---
title: "[Solution] Heroku PHP Build Error"
description: "Fix Heroku PHP build errors. Resolve PHP compilation issues."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["error"]
---

Heroku PHP Build Error can prevent your application from working correctly.

## Common Causes

- Extension missing
- PHP version mismatch
- Composer error

## How to Fix

### Check composer.json

```json
{"require": {"php": ">=8.1"}}
```


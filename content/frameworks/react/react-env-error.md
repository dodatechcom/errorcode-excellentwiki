---
title: "[Solution] React Env Error"
description: "Environment variable not accessible."
frameworks: ["react"]
error-types: ["framework-error"]
severities: ["error"]
---

Environment variable not accessible.

## Common Causes

Not in NEXT_PUBLIC_.

## How to Fix

Use NEXT_PUBLIC_ prefix.

## Example

```javascript
// Only NEXT_PUBLIC_ vars are exposed to client
NEXT_PUBLIC_API_URL=https://api.example.com
```

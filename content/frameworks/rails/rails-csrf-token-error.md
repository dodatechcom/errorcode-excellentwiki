---
title: "[Solution] Rails CSRF Token Error"
description: "CSRF token missing."
frameworks: ["rails"]
error-types: ["framework-error"]
severities: ["error"]
---

CSRF token missing.

## Common Causes

Meta tag missing.

## How to Fix

Include csrf_meta_tags.

## Example

```erb
<%= csrf_meta_tags %>
```

---
title: "[Solution] Apache mod_alias Redirect Loop"
description: "An Alias or Redirect directive creates an infinite redirect loop."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

An Alias or Redirect directive creates an infinite redirect loop.

## Common Causes

- Alias overlaps with DocumentRoot in a loop
- Redirect destination matches the source pattern
- Alias points to a directory that redirects back

## How to Fix

- Verify Alias paths do not overlap with DocumentRoot
- Ensure Redirect destination does not match the source URL
- Use RedirectMatch with careful regex to avoid loops

## Examples

```
['# This causes a loop if /var/www/link points back to /old/\nAlias /old/ /var/www/old/\n# Avoid:\n# Alias /old/ /var/www/link/']
```

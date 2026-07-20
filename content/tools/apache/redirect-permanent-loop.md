---
title: "[Solution] Apache Redirect Permanent Loop"
description: "A Redirect permanent (301) creates an infinite redirect loop."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A Redirect permanent (301) creates an infinite redirect loop.

## Common Causes

- Redirect destination matches the source URL
- Redirect on the same path with a different hostname but both point to same server
- Missing conditions to prevent recursive redirect

## How to Fix

- Use RedirectMatch with conditions
- Ensure destination differs from source
- Test redirect chains with curl -v

## Examples

```
['# Causes loop:\n# RedirectMatch ^/$ /home\n# Fix - be specific:\nRedirect 301 /old-path /new-path']
```

---
title: "[Solution] Apache mod_expires Invalid Configuration"
description: "The ExpiresActive or ExpiresByType directives have invalid syntax or values."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The ExpiresActive or ExpiresByType directives have invalid syntax or values.

## Common Causes

- ExpiresByType uses invalid MIME type
- ExpiresDefault value is not a valid time expression
- ExpiresActive On set but no expiration rules defined

## How to Fix

- Verify MIME types are correct (e.g., text/html)
- Use valid time expressions: access plus 1 month
- Ensure ExpiresActive is On before setting rules

## Examples

```
['ExpiresActive On\nExpiresByType text/html "access plus 1 week"\nExpiresDefault "access plus 1 month"']
```

---
title: "[Solution] Apache AuthType Not Set"
description: "Authentication directives are used without setting AuthType."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Authentication directives are used without setting AuthType.

## Common Causes

- AuthType Basic or Digest missing
- AuthUserFile or AuthGroupFile set without AuthType
- Require valid-user used without authentication setup

## How to Fix

- Add AuthType Basic (or Digest) before other auth directives
- Set AuthName along with AuthType
- Complete authentication configuration before Require

## Examples

```
['AuthType Basic\nAuthName "Restricted Area"\nAuthUserFile /etc/apache2/.htpasswd\nRequire valid-user']
```

---
title: "[Solution] Apache Require valid-user Failed"
description: "The Require valid-user directive fails because no valid user authenticated."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The Require valid-user directive fails because no valid user authenticated.

## Common Causes

- User provided wrong credentials
- AuthUserFile does not contain the user
- Password file is empty or corrupted

## How to Fix

- Verify username exists in AuthUserFile
- Reset password: htpasswd /etc/apache2/.htpasswd username
- Check AuthUserFile path is correct

## Examples

```
['# Add or reset user\nhtpasswd /etc/apache2/.htpasswd username\n# Verify file content\ncat /etc/apache2/.htpasswd']
```

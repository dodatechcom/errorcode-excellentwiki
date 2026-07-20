---
title: "[Solution] Apache mod_userdir Error"
description: "The UserDir directive is misconfigured or user directories are not accessible."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The UserDir directive is misconfigured or user directories are not accessible.

## Common Causes

- UserDir disabled for all users
- User directory does not exist or has wrong permissions
- UserDir path does not match actual home directory layout

## How to Fix

- Enable UserDir for specific users or *
- Ensure home directories have execute permission for Apache
- Configure UserDir to match your home directory structure

## Examples

```
['UserDir public_html\n<Directory /home/*/public_html>\n  AllowOverride All\n  Require all granted\n</Directory>']
```

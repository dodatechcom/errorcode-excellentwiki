---
title: "[Solution] Apache RewriteEngine Not Enabled"
description: "RewriteRule directives are present but RewriteEngine is not turned on."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

RewriteRule directives are present but RewriteEngine is not turned on.

## Common Causes

- RewriteEngine directive is missing or set to Off
- Rewrite rules in .htaccess but AllowOverride does not include FileInfo
- Module loaded but not activated for the context

## How to Fix

- Add RewriteEngine On before any RewriteRule
- Ensure AllowOverride FileInfo or All is set
- Verify mod_rewrite is loaded

## Examples

```
['RewriteEngine On\nRewriteRule ^old-page$ new-page [R=301,L]']
```

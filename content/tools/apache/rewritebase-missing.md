---
title: "[Solution] Apache RewriteBase Missing"
description: "RewriteRule requires RewriteBase but it is not defined."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

RewriteRule requires RewriteBase but it is not defined.

## Common Causes

- RewriteRule in .htaccess without RewriteBase
- Alias causes DocumentRoot mismatch
- Subdirectory rewrites need explicit base

## How to Fix

- Add RewriteBase / before RewriteRule
- Set RewriteBase to the directory path
- Use absolute paths in RewriteRule target

## Examples

```
['RewriteEngine On\nRewriteBase /\nRewriteRule ^old$ new [L]']
```

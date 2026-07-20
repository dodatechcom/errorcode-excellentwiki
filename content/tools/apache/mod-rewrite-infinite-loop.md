---
title: "[Solution] Apache mod_rewrite Infinite Loop"
description: "A RewriteRule creates an infinite loop by repeatedly matching itself."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A RewriteRule creates an infinite loop by repeatedly matching itself.

## Common Causes

- RewriteRule pattern matches the rewritten URL
- Missing RewriteCond to prevent re-matching
- RewriteRule [L] flag not used to stop processing

## How to Fix

- Add RewriteCond %{REQUEST_URI} to prevent re-matching
- Use [L] flag to stop rule processing
- Add [R] flag for external redirects to break loops

## Examples

```
['RewriteEngine On\nRewriteCond %{REQUEST_URI} !^/index\\.php$\nRewriteRule ^(.*)$ /index.php [L]']
```

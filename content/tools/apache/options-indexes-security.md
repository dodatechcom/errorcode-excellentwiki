---
title: "[Solution] Apache Options Indexes Security Risk"
description: "Directory listing is enabled, exposing file structure to visitors."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Directory listing is enabled, exposing file structure to visitors.

## Common Causes

- Options +Indexes allows directory browsing
- No index.html or DirectoryIndex file present
- Sensitive files visible in directory listing

## How to Fix

- Add an index file or set Options -Indexes
- Remove sensitive files from web-accessible directories
- Use Apache autoindex module with careful configuration

## Examples

```
['# Disable directory listing\n<Directory /var/www/html>\n  Options -Indexes +FollowSymLinks\n</Directory>']
```

---
title: "[Solution] Apache FollowSymLinks Not Enabled"
description: "A symbolic link is being followed but FollowSymLinks is not enabled."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

A symbolic link is being followed but FollowSymLinks is not enabled.

## Common Causes

- Options +FollowSymLinks not set
- Options +SymLinksIfOwnerMatch not set
- Symlink points outside DocumentRoot

## How to Fix

- Enable Options +FollowSymLinks or +SymLinksIfOwnerMatch
- Use SymlinksIfOwnerMatch for better security
- Verify symlink targets are accessible

## Examples

```
['<Directory /var/www/html>\n  Options +FollowSymLinks\n</Directory>']
```

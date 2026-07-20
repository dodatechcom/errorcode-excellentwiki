---
title: "[Solution] Apache DirectoryIndex Missing"
description: "No DirectoryIndex is configured or the default index file is not found."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

No DirectoryIndex is configured or the default index file is not found.

## Common Causes

- index.html, index.php etc. do not exist
- DirectoryIndex directive lists no valid files
- File permissions prevent reading the index

## How to Fix

- Create an index file or add your filename to DirectoryIndex
- Ensure the file is readable by Apache
- Check for case sensitivity in filenames

## Examples

```
['DirectoryIndex index.html index.php']
```

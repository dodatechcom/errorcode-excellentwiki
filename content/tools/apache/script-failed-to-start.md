---
title: "[Solution] Apache Script Failed to Start"
description: "The CGI script could not be started by Apache."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The CGI script could not be started by Apache.

## Common Causes

- Script interpreter not found (bad shebang line)
- Script lacks execute permission
- Required libraries not available to the script
- Script file is corrupted

## How to Fix

- Check the shebang line: head -1 script.cgi
- chmod +x the script file
- Verify the interpreter exists at the specified path

## Examples

```
['#!/usr/bin/perl\n# Verify perl exists\nwhich perl']
```

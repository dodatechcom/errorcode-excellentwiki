---
title: "[Solution] Apache CustomLog Pipe Broken"
description: "The CustomLog pipe command is not running or has crashed."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The CustomLog pipe command is not running or has crashed.

## Common Causes

- Piped logging process has exited
- Command in CustomLog pipe is not executable
- Pipe command path is incorrect

## How to Fix

- Restart the piped logging process
- Verify the command exists and is executable
- Check error log for pipe process exit status

## Examples

```
['# Verify pipe command exists\nwhich rotatelogs\n# Use full path\nCustomLog "|/usr/bin/rotatelogs /var/log/apache2/access.log 86400" combined']
```

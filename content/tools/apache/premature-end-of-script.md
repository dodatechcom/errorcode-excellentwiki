---
title: "[Solution] Apache Premature End of Script Headers"
description: "The CGI script closed its output before sending complete HTTP headers."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The CGI script closed its output before sending complete HTTP headers.

## Common Causes

- Script crashes or exits before printing headers
- Script outputs binary data before headers
- Script takes too long and is killed
- Interpreter error in script

## How to Fix

- Ensure script prints Content-Type header first
- Check script for errors: perl -c script.pl
- Increase ScriptTimeout if script needs more time
- Add error logging to the script

## Examples

```
['#!/usr/bin/perl\nprint "Content-type: text/html\\n\\n";\nprint "Hello World\\n";']
```

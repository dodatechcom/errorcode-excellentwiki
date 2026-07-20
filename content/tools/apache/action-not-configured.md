---
title: "[Solution] Apache Action Not Configured"
description: "The Action directive references a handler or CGI script that is not properly configured."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The Action directive references a handler or CGI script that is not properly configured.

## Common Causes

- Handler name in Action does not match a defined handler
- CGI script path is incorrect
- Action used without the required module

## How to Fix

- Verify the handler name matches an existing handler
- Ensure the CGI script exists and is executable
- Load the module that defines the handler

## Examples

```
['Action image/jpeg /cgi-bin/images.cgi\n<FilesMatch "\\.jpg$">\n  SetHandler image/jpeg\n</FilesMatch>']
```

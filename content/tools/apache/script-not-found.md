---
title: "[Solution] Apache CGI Script Not Found"
description: "The requested CGI script does not exist at the specified path."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

The requested CGI script does not exist at the specified path.

## Common Causes

- Script file not uploaded or deployed
- Script path in URL does not match actual file location
- Script permissions are wrong (not executable)
- ScriptHandler or AddHandler not configured

## How to Fix

- Verify script exists at the CGI directory path
- Ensure script has execute permission: chmod +x script.cgi
- Check ScriptAlias or AddHandler configuration

## Examples

```
['# Ensure script is executable\nchmod +x /usr/lib/cgi-bin/script.cgi\n# Check ScriptAlias\nScriptAlias /cgi-bin/ /usr/lib/cgi-bin/']
```

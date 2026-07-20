---
title: "[Solution] Apache CGI Directory Not Configured"
description: "No CGI directory is configured, so CGI scripts cannot be executed."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

No CGI directory is configured, so CGI scripts cannot be executed.

## Common Causes

- No ScriptAlias directive in configuration
- No directory with Options +ExecCGI
- CGI module not loaded

## How to Fix

- Add a ScriptAlias directive for the CGI directory
- Set Options +ExecCGI for the appropriate directory
- Load mod_cgi or mod_cgid

## Examples

```
['ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/\n<Directory /usr/lib/cgi-bin>\n  Options +ExecCGI\n  Require all granted\n</Directory>']
```

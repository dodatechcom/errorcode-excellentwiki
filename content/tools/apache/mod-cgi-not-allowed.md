---
title: "[Solution] Apache mod_cgi Not Allowed"
description: "CGI execution is not permitted in the specified directory."
tools: ["apache"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

CGI execution is not permitted in the specified directory.

## Common Causes

- ScriptAlias not set for the directory
- Options +ExecCGI not enabled
- AddHandler cgi-script not configured
- AllowOverride prevents CGI in .htaccess

## How to Fix

- Set Options +ExecCGI for the CGI directory
- Use ScriptAlias for the CGI directory
- Ensure AllowOverride allows the directives

## Examples

```
['<Directory /usr/lib/cgi-bin>\n  Options +ExecCGI\n  AddHandler cgi-script .cgi .pl\n  Require all granted\n</Directory>']
```

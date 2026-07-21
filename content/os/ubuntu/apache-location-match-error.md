---
title: "Apache Location Match Error"
description: "Apache Location directive matches unexpected URLs or causes redirect loops"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Apache Location Match Error

Apache Location directive matches unexpected URLs or causes redirect loops

## Common Causes

- Location regex pattern incorrect
- LocationMatch vs Location confusion
- Rewrite rules inside Location causing loops
- Case sensitivity issues in Location matching

## How to Fix

1. Test pattern: `apachectl -t` for syntax
2. Check access: `curl -v http://host/path`
3. Review rewrite rules inside Location block
4. Use [L] flag to stop rule processing

## Examples

```apache
# Location match examples
<Location /api>
    ProxyPass http://backend:8080/
    ProxyPassReverse /api/
</Location>

<LocationMatch "^/status$">
    SetHandler server-status
</LocationMatch>
```

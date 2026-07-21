---
title: "[Solution] Grafana Dashboard LDAP Error"
description: "How to fix Grafana LDAP authentication errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- LDAP server unreachable
- Bind DN or password wrong
- User search base incorrect

## How to Fix

```toml
[[servers]]
host = "ldap.example.com"
bind_dn = "cn=admin,dc=example,dc=com"
search_filter = "(cn=%s)"
search_base_dns = ["ou=users,dc=example,dc=com"]
```

## Examples

```bash
ldapsearch -x -H ldap://ldap.example.com -b "ou=users,dc=example,dc=com" "(cn=testuser)"
```

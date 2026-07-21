---
title: "[Solution] Grafana Team Sync Error"
description: "How to fix Grafana team synchronization errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- LDAP group mapping incorrect
- OAuth claim not matching team
- External group not configured

## How to Fix

```ini
[auth.ldap]
enabled = true
config_file = /etc/grafana/ldap.toml
```

## Examples

```bash
ldapsearch -x -H ldap://ldap-server -b "ou=users,dc=example,dc=com" "(cn=admin)"
```

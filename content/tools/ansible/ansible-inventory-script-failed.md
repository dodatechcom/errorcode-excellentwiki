---
title: "[Solution] Ansible Inventory Script Failed"
description: "Fix Ansible dynamic inventory script execution errors"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible dynamic inventory script fails to execute or return valid JSON.

```
ERROR! Failed to parse inventory script
```

## Common Causes

- Script not executable
- Script returns invalid JSON
- Script dependencies missing
- Script timeout

## How to Fix

```bash
# Make script executable
chmod +x inventory_script.py

# Test manually
./inventory_script.py --list
./inventory_script.py --host web1
```

```ini
[defaults]
inventory = ./inventory_script.py
```

```yaml
# Inventory script must return JSON
# --list output:
{
  "webservers": {
    "hosts": ["web1", "web2"],
    "vars": {"http_port": 80}
  }
}

# --host output:
{"ansible_host": "192.168.1.100"}
```

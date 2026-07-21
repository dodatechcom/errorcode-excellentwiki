---
title: "[Solution] YugabyteDB Tablet Firewall Error"
description: "How to fix YugabyteDB tablet firewall errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Firewall blocking inter-node communication
- Port not open
- iptables rule blocking traffic

## How to Fix

```bash
iptables -L -n | grep 7100
```

## Examples

```bash
nc -zv tikv-host 7100
```

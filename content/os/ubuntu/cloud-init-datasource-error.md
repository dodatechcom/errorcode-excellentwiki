---
title: "Cloud-Init Datasource Detection Error"
description: "Cloud-init cannot detect or connect to metadata datasource"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cloud-Init Datasource Detection Error

Cloud-init cannot detect or connect to metadata datasource

## Common Causes

- Cloud provider metadata service unreachable
- Network not configured during cloud-init early stage
- Datasource not configured in cloud-init config
- Timeout waiting for datasource response

## How to Fix

1. Check datasource: `cloud-init query --format json`
2. View logs: `journalctl -u cloud-init`
3. Check config: `cat /etc/cloud/cloud.cfg.d/*.cfg`
4. Force datasource: `datasource_list: [NoCloud]` in cloud.cfg

## Examples

```bash
# Check cloud-init status
cloud-init status

# View cloud-init logs
sudo journalctl -u cloud-init -n 100

# Check detected datasource
cloud-id
```

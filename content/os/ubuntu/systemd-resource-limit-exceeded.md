---
title: "[Solution] Ubuntu Server: systemd-resource-limit-exceeded"
description: "Fix Ubuntu systemd-resource-limit-exceeded. systemd service exceeds resource limits."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Resource Limit Exceeded

systemd enforces resource limits and kills or blocks services.

## Common Causes
- MemoryLimit or CPUQuota set too low
- LimitNOFILE too low for high-traffic service
- LimitNPROC reached for fork-heavy service
- TasksMax exceeded in cgroup

## How to Fix
1. Check current limits
```bash
systemctl show <service> | grep -E "MemoryLimit|CPUQuota|LimitNOFILE"
cat /proc/<PID>/limits
```
2. Override limits
```bash
sudo systemctl edit <service>
[Service]
MemoryLimit=2G
LimitNOFILE=65536
CPUQuota=200%
```
3. Reload and restart
```bash
sudo systemctl daemon-reload
sudo systemctl restart <service>
```

## Examples
```bash
$ journalctl -u mysql
mysql[1234]: Out of memory: Killed process 1234 (mysqld)

$ systemctl show mysql.service | grep MemoryLimit
MemoryLimit=536870912
```

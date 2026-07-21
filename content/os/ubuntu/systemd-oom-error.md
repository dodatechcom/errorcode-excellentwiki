---
title: "[Solution] Ubuntu Server: system-oom-error"
description: "Fix Ubuntu system-oom-error. systemd service killed by OOM killer."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd OOM Error

systemd service is killed by the Out-of-Memory killer.

## Common Causes
- Service memory leak
- Service memory limit set too low
- System under heavy memory load
- No swap space available

## How to Fix
1. Check OOM events
```bash
journalctl -k | grep -i oom
```
2. Check service memory usage
```bash
systemctl show <service> | grep MemoryCurrent
systemctl status <service>
```
3. Increase memory limit
```bash
sudo systemctl edit <service>
[Service]
MemoryMax=4G
OOMPolicy=continue
```

## Examples
```bash
$ journalctl -k | grep -i oom
[ 1234.567] Out of memory: Kill process 1234 (mysql) score 800

$ systemctl show mysql | grep MemoryCurrent
MemoryCurrent=1073741824
```

---
title: "[Solution] Nginx Syslog Connection Error"
description: "Nginx cannot establish a connection to the syslog server for log forwarding."
tools: ["nginx"]
error-types: ["tool-error"]
severities: ["error"]
---

## Description

Nginx cannot establish a connection to the syslog server for log forwarding.

## Common Causes

- **Syslog server unreachable**
- **Firewall blocking**
- **Invalid syslog address**
- **DNS resolution failure**

## How to Fix

1. Check: `nc -zv syslog-server 514`
2. Verify address in config
3. Check firewall
4. Test DNS: `dig syslog-server.example.com +short`

## Examples

**Config:**
```nginx
access_log syslog:server=192.168.1.100:514,facility=local7,tag=nginx main;
```
**Test:**
```bash
nc -zv 192.168.1.100 514
```
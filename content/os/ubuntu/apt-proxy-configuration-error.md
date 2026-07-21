---
title: "[Solution] Ubuntu Server: apt-proxy-configuration-error"
description: "Fix Ubuntu apt-proxy-configuration-error. APT proxy configuration is incorrect or unreachable."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Proxy Configuration Error

APT cannot connect through the configured proxy server.

## Common Causes
- Incorrect proxy URL or port
- Proxy server is down or unreachable
- Authentication required but not configured
- Environment variable conflicts with apt config

## How to Fix
1. Check current proxy settings
```bash
cat /etc/apt/apt.conf.d/95proxy
env | grep -i proxy
```
2. Configure proxy correctly
```bash
echo Acquire::http::Proxy

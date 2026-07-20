---
title: "[Solution] Ansible Proxy Connection Failed"
description: "Fix Ansible connection failures when using HTTP or SOCKS proxies"
tools: ["ansible"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Ansible cannot establish connections through a proxy server.

```
FAILED! => "Connection timed out through proxy"
```

## Common Causes

- Proxy settings not configured
- Proxy authentication required
- Proxy does not support SSH tunneling
- NO_PROXY not set for internal hosts

## How to Fix

```bash
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
export no_proxy=localhost,127.0.0.1,192.168.1.0/24
```

```yaml
[all:vars]
ansible_ssh_common_args='-o ProxyJump=admin@bastion.example.com'
```

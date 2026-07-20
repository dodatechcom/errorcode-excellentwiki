---
title: "[Solution] Jenkins Inbound TCP Agent Error"
description: "Fix Jenkins inbound TCP agent connection errors. Resolve TCP agent port and firewall issues."
tools: ["jenkins"]
error-types: ["tool-error"]
severities: ["error"]
---

# Jenkins Inbound TCP Agent Error

Inbound TCP agents connect on a specific TCP port. Connection errors occur when the port is blocked.

## How to Fix

```bash
# Manage Jenkins > Configure Security > Agent protocols > Enable TCP port
sudo ufw allow 50000/tcp
# Or: sudo iptables -A INPUT -p tcp --dport 50000 -j ACCEPT
```

### Use WebSocket Instead

```bash
# Manage Jenkins > Configure Security > Enable WebSocket
```

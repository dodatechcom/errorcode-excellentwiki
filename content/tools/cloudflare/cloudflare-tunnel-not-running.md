---
title: "[Solution] Cloudflare Tunnel Not Running Error"
description: "Fix Cloudflare tunnel not running errors. Resolve cloudflared process stoppage."
tools: ["cloudflare"]
error-types: ["tool-error"]
severities: ["error"]
---

Cloudflare Tunnel Not Running Error can prevent your application from working correctly.

## Common Causes

- Process crashed
- System resource exhaustion
- Configuration error
- Service not started

## How to Fix

### Start

```bash
cloudflared tunnel run my-tunnel
```

### Run as Service

```bash
cloudflared service install
systemctl start cloudflared
```

### Check Logs

```bash
journalctl -u cloudflared -f
```


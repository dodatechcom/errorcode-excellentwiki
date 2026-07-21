---
title: "[Solution] Grafana Dashboard Certificate Error"
description: "How to fix Grafana TLS certificate errors"
tools: ["grafana"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Self-signed certificate not trusted
- Certificate expired
- Certificate chain incomplete

## How to Fix

```ini
[server]
protocol = https
cert_file = /etc/grafana/certs/grafana.crt
cert_key = /etc/grafana/certs/grafana.key
```

## Examples

```bash
openssl x509 -in /etc/grafana/certs/grafana.crt -noout -dates
```

---
title: "[Solution] YugabyteDB Tablet Load Balancer Error"
description: "How to fix YugabyteDB tablet load balancer errors"
tools: ["yugabyte"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Load balancer not routing to healthy node
- Load balancer health check failing
- Load balancer timeout

## How to Fix

```bash
yb-admin list_tablet_servers
```

## Examples

```bash
curl http://loadbalancer-host:8080/health
```

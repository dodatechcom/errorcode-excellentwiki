---
title: "[Solution] Prometheus cAdvisor Error"
description: "Fix Prometheus cadvisor errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus cAdvisor Error

Prometheus cAdvisor errors occur when container metrics collection fails.

## Why This Happens

- cAdvisor not running
- Metrics not exposed
- Container not found
- Permission denied

## Common Error Messages

- `cadvisor_not_running_error`
- `cadvisor_metrics_error`
- `cadvisor_container_error`
- `cadvisor_permission_error`

## How to Fix It

### Solution 1: Check cAdvisor status

Verify cAdvisor is running:

```bash
docker ps | grep cadvisor
```

### Solution 2: Fix metrics exposure

Ensure cAdvisor exposes metrics:

```bash
curl http://localhost:8080/metrics
```

### Solution 3: Check permissions

Verify cAdvisor has access to container stats.


## Common Scenarios

- **cAdvisor not running:** Start cAdvisor container.
- **Metrics not exposed:** Check cAdvisor configuration.

## Prevent It

- Monitor cAdvisor health
- Configure metrics collection
- Test container metrics

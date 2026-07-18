---
title: "[Solution] Prometheus Remote Write Error"
description: "Fix Prometheus remote write errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Remote Write Error

Prometheus remote write errors occur when data cannot be sent to remote storage backends.

## Why This Happens

- Remote write failed
- Connection refused
- Authentication error
- Queue full

## Common Error Messages

- `remote_write_failed`
- `remote_write_connection_error`
- `remote_write_auth_error`
- `remote_write_queue_full`

## How to Fix It

### Solution 1: Configure remote write

Set up remote write:

```yaml
remote_write:
  - url: "http://remote-storage:9090/api/v1/write"
    queue_config:
      max_samples_per_send: 5000
```

### Solution 2: Check authentication

Verify credentials:

```yaml
remote_write:
  - url: "http://remote-storage:9090/api/v1/write"
    basic_auth:
      username: prometheus
      password: secret
```

### Solution 3: Monitor queue

Check remote write queue depth.


## Common Scenarios

- **Connection refused:** Verify the remote storage is accessible.
- **Queue full:** Increase queue size or optimize write throughput.

## Prevent It

- Monitor remote write
- Set queue configs
- Verify connectivity

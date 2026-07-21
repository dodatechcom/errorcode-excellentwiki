---
title: "[Solution] Prometheus Docker Service Discovery Error"
description: "How to fix Prometheus Docker-based service discovery errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Docker daemon unreachable
- Wrong Docker socket path
- Container not exposing metrics port
- Network mode preventing connection

## How to Fix

Configure Docker SD:

```yaml
scrape_configs:
  - job_name: 'docker'
    docker_sd_configs:
      - host: unix:///var/run/docker.sock
        filters:
          - name: label
            values: ['prometheus=true']
```

Add labels to containers:

```bash
docker run -l prometheus=true -l prometheus.port=8080 my-app
```

## Examples

```bash
# Test Docker socket
curl --unix-socket /var/run/docker.sock http://localhost/containers/json

# List containers with labels
docker ps --filter "label=prometheus=true"

# Check discovered targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.discoveredLabels.__meta_docker_container_label_prometheus != null)'
```

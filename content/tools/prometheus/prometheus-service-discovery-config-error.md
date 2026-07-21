---
title: "[Solution] Prometheus Service Discovery Config Error"
description: "Fix Prometheus service discovery configuration errors. Resolve SD mechanisms failing to discover targets."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Service Discovery Config Error

Prometheus service discovery config errors occur when a service discovery mechanism fails to load or parse its configuration, preventing target discovery.

## Common Causes

- Invalid JSON or YAML in SD configuration file
- Incorrect file_sd file path or permissions
- Consul SD pointing to a non-existent Consul agent
- Kubernetes SD using an invalid API endpoint or token

## How to Fix It

### Solution 1: Validate file_sd configuration

Check the JSON file syntax:

```bash
python3 -m json.tool /etc/prometheus/targets/app.json
```

### Solution 2: Verify Consul connectivity

Test Consul SD connectivity:

```bash
curl -s http://localhost:8500/v1/catalog/services | python3 -m json.tool
```

### Solution 3: Check Kubernetes RBAC for SD

Ensure Prometheus has permissions to list pods:

```bash
kubectl auth can-i list pods --as=system:serviceaccount:monitoring:prometheus
```

### Example file_sd config

```json
[
  {
    "targets": ["app1:8080", "app2:8080"],
    "labels": {
      "env": "production",
      "job": "my-app"
    }
  }
]
```

## Prevent It

- Validate SD config files with json.tool or yamllint
- Test SD connectivity before deploying
- Monitor target discovery count in the Prometheus UI
